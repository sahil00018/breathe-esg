from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import DataSourceUploadSerializer
from .services.csv_processor import process_uploaded_csv


class UploadDataSourceView(APIView):

    def post(self, request):

        serializer = DataSourceUploadSerializer(
            data=request.data
        )

        if serializer.is_valid():

            data_source = serializer.save()

            process_uploaded_csv(data_source)

            return Response(
                {
                    "message": "File uploaded successfully"
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )