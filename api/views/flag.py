import re
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


def update_solved(team, challenge):
  """
  Updates the database points for a given team.
  """
  # Save the time that the challenge was solved.
  timestamp = ChallengeTimestamp.objects.create(team=team, challenge=challenge)
  timestamp.save()

  # Update the team points and last timestamp in the database.
  team.last_timestamp = timestamp.created
  team.save()
  challenge.save()

def check_flag(team, challenge, flag):
  """
  Checks a given flag against the challenge flag.
  """
  # Check if team has already solved the challenge.
  res = team.solved.filter(id=challenge.id)
  error = None

  # If the team has not solved the challenge, check the flag else the team
  # has already solved the challenge so return an error message.
  if not res:
    correct = re.compile(r'^{flag}$'.format(flag=challenge.flag)).match(flag)
    #correct = challenge.flag == flag
    
    # If the user input the correct flag, update the team's correct flag
    # count else update the wrong flags count and return an error.
    if correct:
      team.correct_flags = team.correct_flags + 1
      team.save()

      # update timestamps
      update_solved(team, challenge)
      return True, error
    else:
      error = 'Invalid flag'
      team.wrong_flags = team.wrong_flags + 1
      team.save()
      return False, error
  else:
    error = 'Already solved'
    return False, error


class FlagViewDetail(APIView):
  """
  Manages flag submit and statistics by challenge id requests.
  """
  permission_classes = (AllowAny,)

  def get(self, request, challenge_id, format=None):
    """
    Handles flag submit for challenge id
    """
    return Response(str(request.user))

  def post(self, request, challenge_id, format=None):
    """
    Handles flag submit for challenge id
    """
    #return Response(str(request.user))
    try:
      challenge = Challenge.objects.get(id=challenge_id)
    except ObjectDoesNotExist:
      return Response('Challenge not found')

    if 'flag' not in request.data or not request.data['flag']:
      return Response('Flag not given')

    flag = request.data['flag']

    try:
      if not request.user.team:
        return Response('No team associated with user')
    except ObjectDoesNotExist:
      return Response('No team associated with user')

    team = request.user.team
    success, error = check_flag(team, challenge, flag)
    if success:
      return Response('Correct flag')
    else:
      return Response(error)