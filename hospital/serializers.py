from rest_framework import serializers
from .models import Hospital


class HospitalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hospital
        fields = ['id', 'name', 'email', 'phone', 'user']



