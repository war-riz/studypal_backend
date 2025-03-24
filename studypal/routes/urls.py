from ..view import login, register
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('register', register.RegisterView.as_view(), name='register'), # Register
    path('login', login.LoginView.as_view(), name='login'), # Login
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh access token
    path('token/verify', TokenVerifyView.as_view(), name='token_verify'),  # Verify access token
]