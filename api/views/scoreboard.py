from api.models import *
from api.serializers import *
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework_json_api.views import RelationshipView
from rest_framework_json_api import serializers

  
class ScoreboardViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed.
    """
    permission_classes = (AllowAny,)
    resource_name = 'scoreboard'
    queryset = Scoreboard.objects.all()
    serializer_class = ScoreboardSerializer