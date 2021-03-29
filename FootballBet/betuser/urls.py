
from django.urls import path, include
from .views import *
from rest_framework import routers
router = routers.DefaultRouter()
router.register('register_set', RegisterView)
urlpatterns = [
    path('users/',BetUserView.as_view()),
    path('', include(router.urls)),
    path('register/', RegisterConfirmView.as_view()),

]


