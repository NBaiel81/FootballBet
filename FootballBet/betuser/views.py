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

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import login
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from .serializers import *


class RegisterView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class RegisterConfirmView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            massage = render_to_string('accounts/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            })
            to_email = serializer.data['email']
            email = EmailMessage(subject=mail_subject, body=massage, to=[to_email])
            email.send()
            return Response({"data": "Succesfully"})
        return Response(serializer.errors)


