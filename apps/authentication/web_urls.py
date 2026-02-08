from django.urls import path
from django.contrib.auth import views as auth_views
from .web_views import RegisterView

urlpatterns = [
    # Custom Login Page (overriding default registration/login.html)
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login_page'),
    
    # Custom Register Page
    path('register/', RegisterView.as_view(), name='register_page'),
]
