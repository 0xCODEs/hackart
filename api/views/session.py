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

class SessionView(APIView):
  """
  SessionView APIView
  """
  # TODO: Update permissions
  permission_classes = (AllowAny,)
  def form_response(self, isauthenticated, userid, username, error=""):
    data = {
      'isauthenticated': isauthenticated,
      'userid': userid,
      'username': username
    }
    if error:
      data['message'] = error

    return Response(data)

  def get(self, request, *args, **kwargs):
    # Get the current user
    if request.user.is_authenticated():
      return self.form_response(True, request.user.id, request.user.username)
    return self.form_response(False, None, None)

  def post(self, request, *args, **kwargs):
    # Login
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
      if user.is_active:
        login(request, user)
        return self.form_response(True, user.id, user.username)
      return self.form_response(False, None, None, "Account is suspended")
    return self.form_response(False, None, None, "Invalid username or password")

  def delete(self, request, *args, **kwargs):
    # Logout
    logout(request)
    return Response(status=status.HTTP_204_NO_CONTENT)