from rest_framework import serializers
from .models import Who, Activity


class WhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Who
        fields = '__all__'


# class StatusSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Status
#         fields = '__all__'


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'
