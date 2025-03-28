from ..view import login, register, user
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register', register.RegisterView.as_view(), name='register'), # Register
    path('login', login.LoginView.as_view(), name='login'), # Login
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh access token
    path('user/info', user.UserInfoView.as_view(), name='user_info'),  # Get user info
    path('logout', user.LogoutView.as_view(), name='logout'),  # Logout
]