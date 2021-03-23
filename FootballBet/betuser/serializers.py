from rest_framework import serializers
from .models import BetUser

class BetUserSerializer(serializers.ModelSerializer):
    age = serializers.IntegerField(min_value=18, max_value=100)
    class Meta:
        model = BetUser
        fields = ['full_name','country','wallet','age','email','phone']