from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)
    
    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data) # hash is crypographic it, password is received as text, then "disguised" as hash's so that it is not easily identifiable