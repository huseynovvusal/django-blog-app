from django.urls import path
from .web_views import RegisterView, LoginView, LogoutView

urlpatterns = [
    # Custom Login Page (JWT Cookie Logic)
    path('login/', LoginView.as_view(), name='login_page'),
    
    # Custom Register Page
    path('register/', RegisterView.as_view(), name='register_page'),

    # Custom Logout
    path('logout/', LogoutView.as_view(), name='logout'),
]
