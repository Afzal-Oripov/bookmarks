from django.urls import path, include
from .views import user_login, dashboard, register, edit
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetCompleteView, PasswordResetConfirmView

urlpatterns = [
#  path('login/', LoginView.as_view(), name='login'),
#  path('logout/', LogoutView.as_view(), name='logout'),
#  path('password-change/', PasswordChangeView.as_view(), name='password_change'),
#  path('password-change/done/', PasswordChangeDoneView.as_view(),name='password_change_done'),

#   # url-адреса сброса пароля
#  path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
#  path('password-reset/done/',PasswordResetDoneView.as_view(),name='password_reset_done'),
#  path('password-reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
#  path('password-reset/complete/',PasswordResetCompleteView.as_view(),name='password_reset_complete'),

 path('', include('django.contrib.auth.urls')),
 path('', dashboard, name='dashboard'),
 path('register/', register, name='register'),
 path('edit/', edit, name='edit'),
]
 