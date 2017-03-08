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
    fields = '__all__'