from django import forms
from .models import Image
from django.core.files.base import ContentFile
from django.utils.text import slugify
import requests

class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'url', 'description']
        widgets = {
            'url': forms.HiddenInput,  # Assuming you want to keep URL hidden in the form
        }

    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg', 'png']
        extension = url.rsplit('.', 1)[-1].lower()  # Extract the file extension
        
        if extension not in valid_extensions:
            raise forms.ValidationError('The given URL does not match valid image extensions.')
        
        return url

    def save(self, force_insert=False, force_update=False, commit=True):
        # Create an instance without committing to the database
        image = super().save(commit=False)
        image_url = self.cleaned_data['url']
        name = slugify(image.title)
        extension = image_url.rsplit('.', 1)[-1].lower()
        image_name = f'{name}.{extension}'
        
        # Download the image from the URL and save it to the ImageField
        response = requests.get(image_url)
        response.raise_for_status()  # Ensure the request was successful
        image_content = ContentFile(response.content)
        image.image.save(image_name, image_content, save=False)
        
        # Save the instance to the database
        if commit:
            image.save()
        
        return image
