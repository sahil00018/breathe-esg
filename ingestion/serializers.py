from rest_framework import serializers

from .models import DataSource


class DataSourceUploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = DataSource

        fields = [
            "organization",
            "source_type",
            "uploaded_file",
        ]