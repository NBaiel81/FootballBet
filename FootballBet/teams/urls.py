from django.urls import path, include
from .views import *
from rest_framework import routers
urlpatterns =[
    path('teams/',TeamView.as_view()),
]