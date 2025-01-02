from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["user_ID", "user_name", "user_email", "user_password"]
        
        