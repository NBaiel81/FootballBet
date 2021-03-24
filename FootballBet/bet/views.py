from django.shortcuts import render

from django.shortcuts import render
from rest_framework.response import Response

from .models import Bet
from .serializers import BetSerializer
from rest_framework import views

class BetView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = BetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
