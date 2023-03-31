from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from geopy.exc import GeocoderServiceError
from geopy.geocoders import Nominatim

from .forms import SearchConditionForm, DisasterForm, SignUpForm
from .models import Disaster


def signup(request):
    form = SignUpForm(request.POST)
    errors = []

    if request.method == "POST":
        errors = form.errors

    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.customer.first_name = form.cleaned_data.get('first_name')
        user.customer.last_name = form.cleaned_data.get('last_name')
        user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/')

    return render(request, 'signup.html',
                  {'form': form, 'password_helper': form.fields["password1"].help_text, 'errors': errors})


@login_required
def login(request):
    user = request.user
    if user.is_authenticated & user.is_staff:
        return render(request, 'home.html')
    else:
        return redirect('login')


def goto_index_view(url):
    return HttpResponseRedirect(url)


def logout(request):
    response = goto_index_view('/')
    response.delete_cookie("sessionid")
    return response


def disaster_new(request):
    if request.method == "POST":
        form = DisasterForm(request.POST)
        if form.is_valid():
            disaster = form.save(commit=False)
            disaster.save()
            return redirect('detail', disasterNo=disaster.disasterNo)
    else:
        form = DisasterForm()
    return render(request, 'disaster_edit.html', {'form': form})


def disaster_edit(request, disasterNo):
    disaster = get_object_or_404(Disaster, disasterNo=disasterNo)

    if request.method == "POST":
        form = DisasterForm(request.POST, instance=disaster)
        if form.is_valid():
            disaster = form.save()
            disaster.save()

            return redirect('detail', disasterNo=disaster.disasterNo)
    else:
        form = DisasterForm(instance=disaster)
    return render(request, 'disaster_edit.html', {'form': form, 'disaster': disaster})


def disaster_delete(_request, disasterNo):
    disaster = get_object_or_404(Disaster, disasterNo=disasterNo)
    disaster.delete()
    return redirect('all')


def home(request):
    return render(request, 'home.html')


def disaster_list(request):
    disasters = Disaster.objects.all()
    return render(request, 'all.html', {'disasters': disasters, 'cnt': len(disasters)})


def disaster_detail(request, disasterNo):
    disaster = get_object_or_404(Disaster, disasterNo=disasterNo)

    # Convert text location to lat/long coordinates
    geoLocator = Nominatim(user_agent="disaster_detail")
    geoLocation = None

    try:
        # SSL error occur when run server as 'localhost'
        geoLocation = geoLocator.geocode(disaster.location)
    except GeocoderServiceError:
        print("Error: Geolocation module is not available in your environment.")

    return render(request, 'disaster_detail.html', {
        'disaster': disaster,
        'geoLocation': {
            'latitude': geoLocation.latitude,
            'longitude': geoLocation.longitude
        } if geoLocation else {}
    })


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
        region = request.GET["region"]
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

    return render(request, 'search.html', {'disasters': disasters, 'cnt': len(disasters), 'form': form})


def comparison(request):
    year_rows = Disaster.objects.values('year').annotate(count=Count('disasterNo')).order_by('year')
    type_rows = Disaster.objects.values('type').annotate(count=Count('disasterNo')).order_by('-count')
    continent_rows = Disaster.objects.values('continent').annotate(count=Count('disasterNo')).order_by('-count')
    region_rows = Disaster.objects.values('region').annotate(count=Count('disasterNo')).order_by('-count')

    return render(request, 'comparison.html', {
        'year_rows': year_rows,
        'type_rows': type_rows,
        'continent_rows': continent_rows,
        'region_rows': region_rows
    })


def disaster_map(disasterNo):
    from geopy.geocoders import Nominatim
    from .models import Disaster

    disaster = get_object_or_404(Disaster, disasterNo=disasterNo)

    # Convert text location to lat/long coordinates
    geolocator = Nominatim(user_agent="disaster_detail")
    location = geolocator.geocode(disaster.location)

    disaster.location_lat = location.latitude
    disaster.location_long = location.longitude
    disaster.save()
    return


def chart(request):
    year_rows = Disaster.objects.values('year').annotate(count=Count('disasterNo')).order_by('year')
    type_rows = Disaster.objects.values('type').annotate(count=Count('disasterNo')).order_by('-count')
    continent_rows = Disaster.objects.values('continent').annotate(count=Count('disasterNo')).order_by('-count')
    region_rows = Disaster.objects.values('region').annotate(count=Count('disasterNo')).order_by('-count')

    return render(request, 'chart.html',
                  {'year_rows': {'label': [row["year"] for row in year_rows],
                                 'data': [row["count"] for row in year_rows]},
                   'type_rows': {'label': [row["type"] for row in type_rows],
                                 'data': [row["count"] for row in type_rows]},
                   'continent_rows': {'label': [row["continent"] for row in continent_rows],
                                      'data': [row["count"] for row in continent_rows]},
                   'region_rows': {'label': [row["region"] for row in region_rows],
                                   'data': [row["count"] for row in region_rows]}
                   })
