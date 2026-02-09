import jwt
from django.conf import settings
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken

User = get_user_model()

class JWTAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 1. Try to get User from Access Token Cookie
        access_token = request.COOKIES.get('access_token')
        refresh_token = request.COOKIES.get('refresh_token')
        
        if not request.user.is_authenticated:
            request.user = AnonymousUser()

        if access_token:
            try:
                # Decode token effectively validates signature and expiration
                token = AccessToken(access_token) 
                user_id = token['user_id']
                user = User.objects.get(id=user_id)
                request.user = user
            except (TokenError, InvalidToken, User.DoesNotExist):
                # Access token invalid/expired, try refresh
                if refresh_token:
                    self._refresh_token(request, refresh_token)

        elif refresh_token:
             # No access token but have refresh token (maybe access expired and wasn't sent, or cleared)
             self._refresh_token(request, refresh_token)

        response = self.get_response(request)
        
        # If we refreshed the token in _refresh_token, we stored new access_token in request._new_access_token
        if hasattr(request, '_new_access_token'):
            response.set_cookie(
                'access_token',
                request._new_access_token,
                httponly=True,
                samesite='Lax',
                secure=not settings.DEBUG # Secure in Prod
            )

        return response

    def _refresh_token(self, request, refresh_token_str):
        try:
            refresh = RefreshToken(refresh_token_str)
            new_access_token = str(refresh.access_token)
            
            # Get user from refresh token
            user_id = refresh['user_id']
            user = User.objects.get(id=user_id)
            request.user = user
            
            # Store new token to be set in response cookie
            request._new_access_token = new_access_token
        except (TokenError, InvalidToken, User.DoesNotExist):
            pass # Invalid refresh token, user stays Anonymous
