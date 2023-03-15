from django.shortcuts import render

from .models import Disaster, Type, Subgroup, Continent, Region


def disaster_list(request):
    disasters = Disaster.objects.all()

    return render(request, 'disaster_list.html', {'disasters': disasters})


def disaster_search(request):
    types = Type.objects.all()
    subgroups = Subgroup.objects.all()
    continents = Continent.objects.all()
    regions = Region.objects.all()

    return render(request, 'disaster_search.html',
                  {'types': types, 'subgroups': subgroups, 'continents': continents, 'regions': regions})
