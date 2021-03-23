from django.db import models
from teams.models import TeamA,TeamB
class Match(models.Model):
    statuses = (
        ("haven't started", "haven't started"),
        ('going','going'),
        ('finished', 'finished'),
    )
    statuses1 = (
        ('TeamA won', 'TeamA won'),
        ('TeamB won', 'TeamB won'),
    )
    teamA=models.ForeignKey(TeamA,on_delete=models.SET_NULL,null=True)
    teamB=models.ForeignKey(TeamB,on_delete=models.SET_NULL,null=True)
    match_status=models.CharField(choices=statuses,max_length=20)
    result=models.CharField(choices=statuses1,max_length=20)