from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from .forms import SearchConditionForm
from .models import Disaster


def home(request):
    return render(request, 'home.html')


def disaster_list(request):
    disasters = Disaster.objects.all()
    return render(request, 'all.html', {'disasters': disasters})


def disaster_detail(request, disasterNo):
    disaster = get_object_or_404(Disaster, disasterNo=disasterNo)
    return render(request, 'disaster_detail.html', {'disaster': disaster})


def search(request):
    disasters = []
    country = ''
    continent = ''
    region = ''
    d_type = ''
    order = "year"  # Default display order

    # Get values from query strings
    if "country" in request.GET:
        country = request.GET["country"]
    if "continent" in request.GET:
        continent = request.GET["continent"]
    if "region" in request.GET:
        continent = request.GET["region"]
    if "type" in request.GET:
        d_type = request.GET["type"]
    if "order" in request.GET:
        order = request.GET["order"]

    # Initialise form values
    form = SearchConditionForm(initial={
        'country': country,
        'continent': continent,
        'region': region,
        'type': d_type,
        'order': order,
    })

    # Create WHERE clause from query strings
    where = []
    if country != '':
        where.append(Q(country__contains=country))
    if continent != '':
        where.append(Q(continent=continent))
    if region != '':
        where.append(Q(region_id=region))
    if d_type != '':
        where.append(Q(type_id=d_type))

    # Create ORDER BY clause from query parameters
    if order != '':
        order = order

    # Do not show results in first access (without any conditions)
    if len(request.GET) > 0:
        disasters = Disaster.objects.all().filter(*where).order_by(order)

    return render(request, 'search.html', {'disasters': disasters, 'form': form})


def comparison(request):
    disasters = Disaster.objects.all()
    return render(request, 'comparison.html', {'disasters': disasters})
