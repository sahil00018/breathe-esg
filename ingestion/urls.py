from django.urls import path

from .views import UploadDataSourceView


urlpatterns = [
    path(
        "upload/",
        UploadDataSourceView.as_view()
    ),
]