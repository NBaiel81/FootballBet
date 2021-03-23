from rest_framework import serializers
from .models import Match

class MatchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Match
        fields = ['teamA','teamB','match_status','result']