from django.views.generic.edit import CreateView, FormView
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.forms import AuthenticationForm
from django.views import View

from django.contrib.auth import get_user_model
User = get_user_model()

from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email")

class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('blog_web:list')

    def form_valid(self, form):
        # Auto-login after register (JWT Style)
        user = form.save()
        login(self.request, user) # Optional: fires user_logged_in signal
        
        response = redirect(self.success_url)
        
        # Generate Tokens
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)
        
        # Set Cookies
        response.set_cookie('access_token', access_token, httponly=True, secure=not settings.DEBUG, samesite='Lax')
        response.set_cookie('refresh_token', refresh_token, httponly=True, secure=not settings.DEBUG, samesite='Lax')
        
        return response

class LoginView(FormView):
    template_name = 'registration/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('blog_web:list')

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user) # Optional
        
        next_url = self.request.GET.get('next') or self.success_url
        response = redirect(next_url)

        # Generate Tokens
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        # Set Cookies
        response.set_cookie('access_token', access_token, httponly=True, secure=not settings.DEBUG, samesite='Lax')
        response.set_cookie('refresh_token', refresh_token, httponly=True, secure=not settings.DEBUG, samesite='Lax')

        return response

class LogoutView(View):
    def post(self, request):
        logout(request) # Clears session (if any)
        response = redirect('blog_web:list')
        response.delete_cookie('access_token')
        response.delete_cookie('refresh_token')
        return response
