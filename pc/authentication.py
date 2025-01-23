from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

API_KEY="sdkgfbkfckkngklkjkeyrterytcaxmslk"

class APIKeyAuthentication (BaseAuthentication):
    def authenticate(self,request):
        api_key=request.headers.get('X-API-KEY')

        print(f"Received API Key: {api_key}")

        if not api_key:
            raise AuthenticationFailed('API key missing')

        if api_key !=API_KEY:
            raise AuthenticationFailed('Inavalid Api key')
        return None