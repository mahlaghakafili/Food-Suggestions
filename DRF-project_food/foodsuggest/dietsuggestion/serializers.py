from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'bmi', 'name', 'fname', 'email', 'contact', 'veg_type']
