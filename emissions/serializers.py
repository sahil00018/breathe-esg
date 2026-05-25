from rest_framework import serializers
from .models import NormalizedEmissionRecord


class EmissionRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = NormalizedEmissionRecord
        fields = "__all__"