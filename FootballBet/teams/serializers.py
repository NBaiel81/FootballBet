from rest_framework import serializers
from .models import Team

class TeamSerializer(serializers.ModelSerializer):
    stars = serializers.IntegerField(min_value=0, max_value=5)

    class Meta:
        model = Team
        fields = ['name','logo','stars','country','wins','loses']
