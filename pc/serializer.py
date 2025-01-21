from .models import product
from rest_framework.serializers import ModelSerializer

class prodserializer(ModelSerializer):
    class Meta:
        model=product
        fields='__all__'