from django.shortcuts import render

from django.shortcuts import render
from rest_framework.response import Response

from .models import Match
from .serializers import MatchSerializer
from rest_framework import views

class MatchView(views.APIView):
    def get(self, request, *args, **kwargs):
        matches=Match.objects.all()
        serializer = MatchSerializer(matches, many=True)
        return Response(serializer.data)
