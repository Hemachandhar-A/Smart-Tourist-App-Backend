from rest_framework import authentication
from rest_framework import exceptions
from django.conf import settings

class APIKeyAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        api_key = request.headers.get('X-API-Key')
        if not api_key:
            raise exceptions.AuthenticationFailed('Access Not Permitted.')
        
        if api_key != settings.ADMIN_API_KEY:
            raise exceptions.AuthenticationFailed('Invalid API Key.')
        
        return (None, None)
    