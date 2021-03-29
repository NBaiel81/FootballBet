from django.db import models
from betuser.models import BetUser
from match.models import Match
# Create your models here.
class Bet(models.Model):
    statuses = (
        ('TeamA won', 'TeamA won'),
        ('TeamB won', 'TeamB won'),
    )
    game = (
        ('normal bet', 'normal bet'),
        ('super bet','super bet'),
    )
    bet_type=models.CharField(choices=game,max_length=20)
    betuser=models.ForeignKey(BetUser,on_delete=models.SET_NULL,null=True)
    bet_amount=models.PositiveIntegerField()
    date_created=models.DateTimeField(auto_now_add=True)
    match=models.ForeignKey(Match,on_delete=models.SET_NULL,null=True)
    result=models.CharField(choices=statuses,max_length=20)
    TeamA_score = models.PositiveIntegerField(default=0, blank=True)
    TeamB_score = models.PositiveIntegerField(default=0, blank=True)
