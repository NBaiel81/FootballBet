from rest_framework import serializers
from .models import Match

class MatchSerializer(serializers.ModelSerializer):
    match=serializers.SerializerMethodField()
    class Meta:
        model = Match
        fields = ['teamA','teamB','match_status','result','match']
    def get_match(self,obj):
        if obj.match_status =='finished':
            bets=obj.bet_set.all()
            for bet in bets:
                print(obj.result)
                if bet.result == obj.result:
                    bet.betuser.wallet += bet.bet_amount * 2
                    bet.betuser.save()







class MatcUpdateSerializer(serializers.Serializer):
    statuses = (
        ("haven't started", "haven't started"),
        ('going', 'going'),
        ('finished', 'finished'),
    )
    match_status=serializers.ChoiceField(choices=statuses)

