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

class ChallengeViewSet(viewsets.ModelViewSet):
  """
  Challenge APIView
  """
  # TODO: Update permissions
  permission_classes = (AllowAny,)
  queryset = Challenge.objects.all()
  serializer_class = ChallengeSerializer  
