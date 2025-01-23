from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
import os
API_KEY=os.getenv("API_KEY")

class APIKeyAuthentication (BaseAuthentication):
    def authenticate(self,request):
        api_key=request.headers.get('api-key')

        print(f"Received API Key: {api_key}")

        if not api_key:
            raise AuthenticationFailed('API key missing')

        if api_key !=API_KEY:
            raise AuthenticationFailed('Inavalid Api key')
        return None