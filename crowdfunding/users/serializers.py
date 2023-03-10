from rest_framework import serializers
from .models import CustomUser
from django.utils import timezone

class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)
    password = serializers.CharField(write_only = True) 
    bio = serializers.CharField() #create users bio
    image = serializers.URLField()
    date_joined = serializers.DateTimeField(default=timezone.now)
    
    
    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data) # hash is crypographic it, password is received as text, then "disguised" as hash's so that it is not easily identifiable
