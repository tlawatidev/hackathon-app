from django.shortcuts import render

from records.models import Record


def dashboard(request, *args, **kwargs):
    template = "hackathonapp/dashboard.html"
    data = {"records_total": Record.objects.count()}
    return render(request, template, data)
