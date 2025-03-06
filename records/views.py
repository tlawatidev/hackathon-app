from django.views import generic

from records.models import Record


class RecordListView(generic.ListView):
    model = Record
    template_name = "records/record_list.html"


class RecordDetailView(generic.DetailView):
    model = Record
    template_name = "records/record_detail.html"
