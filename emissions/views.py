from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import NormalizedEmissionRecord
from .serializers import EmissionRecordSerializer
from django.db.models import Count

class PendingRecordsView(APIView):

    def get(self, request):

        records = NormalizedEmissionRecord.objects.filter(
            status="PENDING"
        )

        serializer = EmissionRecordSerializer(records, many=True)

        return Response(serializer.data)
class ApproveRecordView(APIView):

    def post(self, request, pk):

        record = NormalizedEmissionRecord.objects.get(id=pk)

        record.status = "APPROVED"
        record.locked_for_audit = True
        record.save()

        return Response({"message": "Record approved"})
class RejectRecordView(APIView):

    def post(self, request, pk):

        record = NormalizedEmissionRecord.objects.get(id=pk)

        record.status = "REJECTED"
        record.save()

        return Response({"message": "Record rejected"})
    
class DashboardStatsView(APIView):

    def get(self, request):

        data = NormalizedEmissionRecord.objects.values("status") \
            .annotate(count=Count("id"))

        stats = {
            "PENDING": 0,
            "APPROVED": 0,
            "REJECTED": 0
        }

        for item in data:
            stats[item["status"]] = item["count"]

        return Response(stats)