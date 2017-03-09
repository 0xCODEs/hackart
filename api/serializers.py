#from rest_framework import serializers
from rest_framework_json_api import serializers
from api.models import *
from django.contrib.auth.models import User
from rest_framework_json_api.relations import ResourceRelatedField


class ChallengeSerializer(serializers.ModelSerializer):
  """
  Sets fields for the rest api to serialize in the Challenge model.
  """
  class Meta:
    model = Challenge
    fields = ('id', 'title', 'points', 'description', 'solved', 'numsolved')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        resource_name = 'users'
        model = User
        fields = ('id', 'username', 'email', 'password', 'is_staff')

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        resource_name = 'teams'
        model = Team
        fields = "__all__"

class ScoreboardSerializer(serializers.ModelSerializer):
  """
  Sets fields for the rest api to serialize in the Scoreboard model.
  """
  class Meta:
    model = Scoreboard
    fields = ('id', 'numtopteams', 'teams')