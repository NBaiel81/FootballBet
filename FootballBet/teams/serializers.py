from rest_framework import serializers
from .models import Team
from match.models import Match
from match.serializers import *
class TeamSerializer(serializers.ModelSerializer):
    stars = serializers.IntegerField(min_value=0, max_value=5)
    teams = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = ['name','logo','stars','country','wins','loses','teams']

    def get_teams(self,obj):
        teamA=Match.objects.filter(teamA__team__name=obj.name)

        for team in teamA:
            if team.match_status == "finished":
                if team.result == "TeamA won" and team.teamA.team.name == obj.name:
                    print(1)
                    obj.wins+=1
                    obj.save()

            elif team.result == "TeamB won" and team.teamA.team.name == obj.name:
                obj.loses+=1
                obj.save()

        teamB = Match.objects.filter(teamB__team__name=obj.name)
        for team in teamB:
            if team.match_status == "finished":
                if team.result == "TeamB won" and team.teamB.team.name == obj.name:
                    obj.wins += 1
                    obj.save()

                elif team.result == "TeamA won" and team.teamB.team.name == obj.name:
                    obj.loses += 1
                    obj.save()







