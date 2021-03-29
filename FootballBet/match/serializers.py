from rest_framework import serializers
from .models import Match

class MatchSerializer(serializers.ModelSerializer):
    match=serializers.SerializerMethodField()
    result = serializers.CharField(read_only=True)
    score = serializers.SerializerMethodField()
    class Meta:
        model = Match
        fields = ['teamA','teamB','match_status','result','match','id','TeamA_score','TeamB_score','score']
    def get_score(self,obj):
        if obj.TeamA_score > obj.TeamB_score:
            obj.result="TeamA won"
        elif obj.TeamA_score < obj.TeamB_score:
            obj.result="TeamB won"
        obj.save()

    def get_match(self,obj):
        if obj.match_status =='finished':
            bets=obj.bet_set.all()
            coef_A = obj.bet_set.filter(result='TeamA won').count()
            coef_B = obj.bet_set.filter(result='TeamB won').count()


            for bet in bets:
                if bet.bet_type =="normal bet":
                    print(obj.result)
                    if coef_A == 0 or coef_B == 0:
                        if bet.result == 'TeamA won' and bet.result == obj.result:
                            bet.betuser.wallet += (bet.bet_amount * 2) +bet.bet_amount
                            bet.betuser.save()
                        elif bet.result == 'TeamB won' and bet.result == obj.result:
                            bet.betuser.wallet += (bet.bet_amount * 2) +bet.bet_amount
                            bet.betuser.save()
                    else:
                        if bet.result == 'TeamA won' and bet.result == obj.result:
                            bet.betuser.wallet += (bet.bet_amount * (coef_B/coef_A)) +bet.bet_amount
                            bet.betuser.save()
                        elif bet.result == 'TeamB won' and bet.result == obj.result:
                            bet.betuser.wallet += bet.bet_amount * (coef_A / coef_B) +bet.bet_amount
                            bet.betuser.save()
                elif bet.bet_type=="super bet":
                    print(1)
                    if coef_A == 0 or coef_B == 0:
                        if bet.TeamA_score ==obj.TeamA_score and bet.TeamB_score == obj.TeamB_score:
                            bet.betuser.wallet += (bet.bet_amount * 2)*5 +bet.bet_amount
                            bet.betuser.save()
                        elif bet.TeamA_score ==obj.TeamA_score and bet.TeamB_score == obj.TeamB_score:
                            bet.betuser.wallet += (bet.bet_amount * 2)*5 +bet.bet_amount
                            bet.betuser.save()
                    else:
                        if bet.TeamA_score ==obj.TeamA_score and bet.TeamB_score == obj.TeamB_score:
                            bet.betuser.wallet += (bet.bet_amount * (coef_B/coef_A))*5 +bet.bet_amount
                            bet.betuser.save()
                        elif bet.TeamA_score ==obj.TeamA_score and bet.TeamB_score == obj.TeamB_score:
                            bet.betuser.wallet += bet.bet_amount * (coef_A / coef_B)*5 +bet.bet_amount
                            bet.betuser.save()

class MatchUpdateSerializer(serializers.Serializer):
    statuses = (
        ("haven't started", "haven't started"),
        ('going', 'going'),
        ('finished', 'finished'),
    )
    match_status=serializers.ChoiceField(choices=statuses)

