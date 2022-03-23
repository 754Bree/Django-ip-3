from rest_framework import serializers
from .models import *


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'image', 'bio')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('author', 'image', 'description','created_date','title','link')