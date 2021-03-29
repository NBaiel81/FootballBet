from rest_framework import serializers
from .models import BetUser

class BetUserSerializer(serializers.ModelSerializer):
    age = serializers.IntegerField(min_value=18, max_value=100)
    class Meta:
        model = BetUser
        fields = ['full_name','country','wallet','age','email','phone']

from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        if password != validated_data.pop('confirm_password'):
            raise ValidationError("NOT OK!!")
        user = User(username=validated_data.pop('username'), email=validated_data.pop('email'))
        user.set_password(password)
        user.save()
        return user