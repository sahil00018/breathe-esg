from django.urls import path
from .views import DashboardStatsView

from .views import (
    PendingRecordsView,
    ApproveRecordView,
    RejectRecordView
)

urlpatterns = [
    path("pending/", PendingRecordsView.as_view()),
    path("approve/<int:pk>/", ApproveRecordView.as_view()),
    path("reject/<int:pk>/", RejectRecordView.as_view()),
    path("stats/", DashboardStatsView.as_view()),
]