from rest_framework import serializers

from .models import *

class statusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = "__all__"

class childSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = "__all__"