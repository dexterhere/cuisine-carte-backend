from django.urls import path
from accounts.views import UserRegistrationView, UserLoginView, UserProfileView, UserChangePasswordView, SendPasswordView, UserPasswordResetView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('changepassword/', UserChangePasswordView.as_view(), name='profile'),
    path('resetpassword/', SendPasswordView.as_view(), name='resetpassword'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name="change-password"),
]
