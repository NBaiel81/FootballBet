from django.db import models

class Team(models.Model):
    name=models.CharField(max_length=30)
    logo=models.ImageField()
    stars=models.PositiveIntegerField(default=0)
    country=models.CharField(max_length=30)
    wins=models.PositiveIntegerField(default=0)
    loses=models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.name

class TeamA(models.Model):
    team=models.ForeignKey(Team,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.team.name

class TeamB(models.Model):
    team=models.ForeignKey(Team,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.team.name

