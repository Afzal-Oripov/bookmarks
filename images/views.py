from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm

@login_required
def image_create(request):
    if request.method == 'POST':
        # Form was submitted
        form = ImageCreateForm(request.POST, request.FILES)
        if form.is_valid():
            # Form data is valid
            cd = form.cleaned_data
            new_image = form.save(commit=False)
            # Assign the current user to the image
            new_image.user = request.user
            new_image.save()
            messages.success(request, 'Image added successfully')
            # Redirect to the detailed view of the newly created image
            return redirect(new_image.get_absolute_url())
        else:
            # Form data is invalid, re-render the form with errors
            messages.error(request, 'Please correct the errors below.')
    else:
        # Form is being displayed for the first time
        form = ImageCreateForm()

    return render(request, 'images/image/create.html', {'section': 'images','form': form })
