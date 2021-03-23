from django.shortcuts import render
from rest_framework.response import Response

from .models import BetUser
from .serializers import BetUserSerializer
from rest_framework import views

class BetUserView(views.APIView):
    def get(self, request, *args, **kwargs):
        users=BetUser.objects.get(user=request.user)
        serializer = BetUserSerializer(users)
        return Response(serializer.data)
