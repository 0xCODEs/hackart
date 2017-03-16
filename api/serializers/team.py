#from rest_framework import serializers
from edctf.api.models import Team
from rest_framework_json_api import serializers
from rest_framework_json_api.relations import ResourceRelatedField


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        resource_name = 'teams'
        model = Team
        fields = "__all__"