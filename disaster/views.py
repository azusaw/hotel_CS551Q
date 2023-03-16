from django.shortcuts import render, get_object_or_404

from .models import Disaster, Type, Subgroup, Continent, Region


def home(request):
    return render(request, 'home.html')


def disaster_list(request):
    disasters = Disaster.objects.all()
    return render(request, 'disaster_list.html', {'disasters': disasters})


def disaster_detail(request, disasterNo):
    disaster = get_object_or_404(Disaster, disasterNo=disasterNo)
    return render(request, 'disaster_detail.html', {'disaster': disaster})


def disaster_search(request):
    types = Type.objects.all()
    subgroups = Subgroup.objects.all()
    continents = Continent.objects.all()
    regions = Region.objects.all()
    return render(request, 'disaster_search.html',
                  {'types': types, 'subgroups': subgroups, 'continents': continents, 'regions': regions})
