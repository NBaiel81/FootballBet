from django.shortcuts import render
from rest_framework.response import Response

from .models import Team
from .serializers import TeamSerializer
from rest_framework import views

class TeamView(views.APIView):
    def get(self, request, *args, **kwargs):
        teams=Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)
