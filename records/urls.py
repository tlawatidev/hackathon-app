from django.urls import path

from records.views import RecordDetailView, RecordListView

app_name = "records"
urlpatterns = [
    path("all/", RecordListView.as_view(), name="record-list"),
    path("<int:pk>/", RecordDetailView.as_view(), name="record-detail"),
]
