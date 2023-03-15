from django.shortcuts import render
from .models import Disaster


def disaster_list(request):
    disasters = Disaster.objects.all()
    return render(request, 'disaster_list.html', {'disasters' : disasters})
