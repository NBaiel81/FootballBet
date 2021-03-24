from django.shortcuts import render

from django.shortcuts import render
from rest_framework.response import Response

from .models import Match
from .serializers import *
from rest_framework import views

class MatchView(views.APIView):
    def get(self, request, *args, **kwargs):
        matches=Match.objects.all()
        serializer = MatchSerializer(matches, many=True)
        return Response(serializer.data)

class MatchUpdateView(views.APIView):
    def get(self,request,*args,**kwargs):
        matches = Match.objects.get(id=kwargs['match_id'])
        serializer = MatchSerializer(matches)
        return Response(serializer.data)

    def put(self,request,*args,**kwargs):
        matches = Match.objects.get(id=kwargs['match_id'])
        serializer=MatchSerializer(matches,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)




