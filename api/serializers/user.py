#from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_json_api import serializers
from rest_framework_json_api.relations import ResourceRelatedField


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        resource_name = 'users'
        model = User
        fields = ('id', 'username', 'email', 'password', 'is_staff')
