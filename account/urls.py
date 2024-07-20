from django.urls import path
from .views import user_login, dashboard
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
 path('logout/', LogoutView.as_view(), name='logout'),
 path('login/', LoginView.as_view(), name='login'),
 path('', dashboard, name='dashboard'),
]