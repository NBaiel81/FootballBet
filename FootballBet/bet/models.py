from django.db import models
from betuser.models import BetUser
from match.models import Match
# Create your models here.
class Bet(models.Model):
    statuses = (
        ('TeamA won', 'TeamA won'),
        ('TeamB won', 'TeamB won'),
    )
    betuser=models.ForeignKey(BetUser,on_delete=models.SET_NULL,null=True)
    bet_amount=models.PositiveIntegerField()
    date_created=models.DateTimeField(auto_now_add=True)
    match=models.ForeignKey(Match,on_delete=models.SET_NULL,null=True)
    result=models.CharField(choices=statuses,max_length=20)