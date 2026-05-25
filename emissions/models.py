from django.db import models

from organizations.models import Organization
from ingestion.models import RawRecord


class NormalizedEmissionRecord(models.Model):

    REVIEW_STATUS = [
        ("PENDING", "PENDING"),
        ("FLAGGED", "FLAGGED"),
        ("APPROVED", "APPROVED"),
        ("REJECTED", "REJECTED"),
        ("LOCKED", "LOCKED"),
    ]

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE
    )

    raw_record = models.ForeignKey(
        RawRecord,
        on_delete=models.CASCADE
    )

    scope = models.CharField(max_length=20)

    category = models.CharField(max_length=100)

    activity_date = models.DateField()

    quantity = models.FloatField()

    unit = models.CharField(max_length=50)

    normalized_unit = models.CharField(max_length=50)

    normalized_quantity = models.FloatField()

    co2e = models.FloatField(
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=REVIEW_STATUS,
        default="PENDING"
    )

    locked_for_audit = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )