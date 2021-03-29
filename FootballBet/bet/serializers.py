from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Bet
from betuser.models import BetUser
class BetSerializer(serializers.ModelSerializer):
    bet_amount = serializers.IntegerField(min_value=100)
    bet_money = serializers.SerializerMethodField()

    class Meta:
        model = Bet
        fields = ['betuser','bet_amount','date_created','match','result','bet_money','TeamA_score','TeamB_score','bet_type']

    def get_bet_money(self,obj):
        bet_money = obj.bet_amount
        if obj.match.match_status == "haven't started":
            if obj.betuser.wallet >= bet_money:
                obj.betuser.wallet -= bet_money
                obj.betuser.save()
            else:
                obj.delete()
                raise ValidationError("Not enough money ")
        else:
            obj.delete()
            raise ValidationError("Time is up")
        # bets = Bet.objects.all()
        # for bet in bets:
        #     if bet.betuser == obj.betuser and bet.result != obj.result and obj.match.match_status == "haven't started":
        #         print(1)
        #         if obj.betuser.wallet >= bet_money:
        #             obj.betuser.wallet -= bet_money
        #             obj.betuser.save()
        #         else:
        #             obj.delete()
        #             raise ValidationError("Not enough money!")
