#from rest_framework import serializers
from api.models import Scoreboard
from rest_framework_json_api import serializers
from rest_framework_json_api.relations import ResourceRelatedField


class ScoreboardSerializer(serializers.ModelSerializer):
  """
  Sets fields for the rest api to serialize in the Scoreboard model.
  """
  class Meta:
    model = Scoreboard
    fields = ('id', 'numtopteams', 'teams')