from django.urls import path
from .views import (
    PublicEndpoint,
    ProtectedEndpoint,
    UserRegistrationView,
    LoginView,
    LogoutView,
    login_page
)

urlpatterns = [
    path('public/', PublicEndpoint.as_view(), name='public-endpoint'),
    path('protected/', ProtectedEndpoint.as_view(), name='protected-endpoint'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('api/login/', LoginView.as_view(), name='api-login'),
    path('api/logout/', LogoutView.as_view(), name='api-logout'),
    path('login/', login_page, name='login-page'),
]