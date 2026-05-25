from django.db import models

from emissions.models import NormalizedEmissionRecord


class AuditLog(models.Model):

    record = models.ForeignKey(
        NormalizedEmissionRecord,
        on_delete=models.CASCADE
    )

    action = models.CharField(
        max_length=100
    )

    old_values = models.JSONField(
        null=True,
        blank=True
    )

    new_values = models.JSONField(
        null=True,
        blank=True
    )

    timestamp = models.DateTimeField(
        auto_now_add=True
    )