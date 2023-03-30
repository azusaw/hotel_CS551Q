from django.db.models import Count, Q
from django.shortcuts import redirect, render, get_object_or_404
from geopy.exc import GeocoderServiceError
from geopy.geocoders import Nominatim
from .models import Disaster
from .forms import SearchConditionForm, DisasterForm



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
    data = Disaster.objects.all()

    Asia = 0
    Americas= 0
    Europe = 0
    Africa = 0
    Oceania = 0

    for con in data:
        if con.continent_id == 'Asia':
            Asia += 1
            print('Asia:', Asia)
        elif con.continent_id == 'Americas':
            Americas += 1
            print('Americas:', Americas)
        elif con.continent_id == 'Europe':
            Europe += 1
            print('Europe:', Europe)
        elif con.continent_id == 'Africa':
            Africa += 1
            print('Africa:', Africa)
        else:
            Oceania += 1
            print('Oceania:', Oceania)


    Storm = 0
    Flood = 0
    Earthquake =0
    Wildfire = 0
    Landslide = 0
    Extreme = 0
    Volcanic = 0
    Drought = 0
    Mass = 0
    Glacial = 0

    for t in data:
        if t.type_id == 'Storm':
            Storm += 1
            print('Storm',Storm)
        elif t.type_id == 'Flood':
            Flood += 1
            print('Flood',Flood)
        elif t.type_id == 'Earthquake':
            Earthquake += 1
        elif t.type_id == 'Wildfire':
            Wildfire += 1
        elif t.type_id == 'Landslide':
            Landslide += 1
        elif t.type_id == 'Glacial lake outburst':
            Glacial += 1
            print('Extreme',Extreme)
        elif t.type_id == 'Volcanic activity':
            Volcanic += 1
        elif t.type_id == 'Drought':
            Drought += 1
        elif t.type_id == 'Mass movement (dry)':
            Mass += 1
        else:
            Extreme += 1

    y1970 = 0
    y1971 = 0
    y1972 = 0
    y1973 = 0
    y1974 = 0
    y1975 = 0
    y1976 = 0
    y1977 = 0
    y1978 = 0
    y1979 = 0
    y1980 = 0
    y1981 = 0
    y1982 = 0
    y1983 = 0
    y1984 = 0
    y1985 = 0
    y1986 = 0
    y1987 = 0
    y1988 = 0
    y1989 = 0
    y1990 = 0
    y1991 = 0
    y1992 = 0
    y1993 = 0
    y1994 = 0
    y1995 = 0
    y1996 = 0
    y1997 = 0
    y1998 = 0
    y1999 = 0
    y2000 = 0
    y2001 = 0
    y2002 = 0
    y2003 = 0
    y2004 = 0
    y2005 = 0
    y2006 = 0
    y2007 = 0
    y2008 = 0
    y2009 = 0
    y2010 = 0
    y2011 = 0
    y2012 = 0
    y2013 = 0
    y2014 = 0
    y2015 = 0
    y2016 = 0
    y2017 = 0
    y2018 = 0
    y2019 = 0
    y2020 = 0
    y2021 = 0

    for y in data:
        if y.year == 1970:
            y1970 += 1
        elif y.year == 1971:
            y1971 += 1
        elif y.year == 1972:
            y1972 += 1
        elif y.year == 1973:
            y1973 += 1
        elif y.year == 1974:
            y1974 += 1
        elif y.year == 1975:
            y1975 += 1
        elif y.year == 1976:
            y1976 += 1
        elif y.year == 1977:
            y1977 += 1
        elif y.year == 1978:
            y1978 += 1
        elif y.year == 1979:
            y1979 += 1
        elif y.year == 1980:
            y1980 += 1
        elif y.year == 1981:
            y1981 += 1
        elif y.year == 1982:
            y1982 += 1
        elif y.year == 1983:
            y1983 += 1
        elif y.year == 1984:
            y1984 += 1
        elif y.year == 1985:
            y1985 += 1
        elif y.year == 1986:
            y1986 += 1
        elif y.year == 1987:
            y1987 += 1
        elif y.year == 1988:
            y1988 += 1
        elif y.year == 1989:
            y1989 += 1
        elif y.year == 1990:
            y1990 += 1
        elif y.year == 1991:
            y1991 += 1
        elif y.year == 1992:
            y1992 += 1
        elif y.year == 1993:
            y1993 += 1
        elif y.year == 1994:
            y1994 += 1
        elif y.year == 1995:
            y1995 += 1
        elif y.year == 1996:
            y1996 += 1
        elif y.year == 1997:
            y1997 += 1
        elif y.year == 1998:
            y1998 += 1
        elif y.year == 1999:
            y1999 += 1
        elif y.year == 2000:
            y2000 += 1
        elif y.year == 2001:
            y2001 += 1
        elif y.year == 2002:
            y2002 += 1
        elif y.year == 2003:
            y2003 += 1
        elif y.year == 2004:
            y2004 += 1
        elif y.year == 2005:
            y2005 += 1
        elif y.year == 2006:
            y2006 += 1
        elif y.year == 2007:
            y2007 += 1
        elif y.year == 2008:
            y2008 += 1
        elif y.year == 2009:
            y2009 += 1
        elif y.year == 2010:
            y2010 += 1
        elif y.year == 2011:
            y2011 += 1
        elif y.year == 2012:
            y2012 += 1
        elif y.year == 2013:
            y2013 += 1
        elif y.year == 2014:
            y2014 += 1
        elif y.year == 2015:
            y2015 += 1
        elif y.year == 2016:
            y2016 += 1
        elif y.year == 2017:
            y2017 += 1
        elif y.year == 2018:
            y2018 += 1
        elif y.year == 2019:
            y2019 += 1
        elif y.year == 2020:
            y2020 += 1
        else:
            y2021 += 1

    EasternAsia = 0
    SouthEasternAsia = 0
    NorthernAmerica = 0
    SouthernAsia = 0
    SouthAmerica = 0
    CentralAmerica = 0
    SouthernEurope = 0
    WesternEurope = 0
    Caribbean = 0
    EasternEurope = 0
    EasternAfrica = 0
    AustraliaandNewZealand = 0
    WesternAsia = 0
    NorthernEurope = 0
    Melanesia = 0
    NorthernAfrica = 0
    WesternAfrica = 0
    SouthernAfrica = 0
    CentralAsia = 0
    Polynesia = 0
    RussianFederation = 0
    MiddleAfrica = 0
    Micronesia = 0

    for r in data:
        if r.region_id == 'Eastern Asia':
            EasternAsia += 1
        elif r.region_id == 'South-Eastern Asia':
            SouthEasternAsia += 1
        elif r.region_id == 'Northern America':
            NorthernAmerica += 1
        elif r.region_id == 'Southern Asia':
            SouthernAsia += 1
        elif r.region_id == 'South America':
            SouthAmerica += 1
        elif r.region_id == 'Central Americ':
            CentralAmerica += 1
        elif r.region_id == 'Southern Europe':
            SouthernEurope += 1
        elif r.region_id == 'Western Europe':
            WesternEurope += 1
        elif r.region_id == 'Caribbean':
            Caribbean+= 1
        elif r.region_id == 'Eastern Europe':
            EasternEurope += 1
        elif r.region_id == 'Eastern Africa':
            EasternAfrica += 1
        elif r.region_id == 'Australia and New Zealand':
            AustraliaandNewZealand += 1
        elif r.region_id == 'Western Asia':
            WesternAsia += 1
        elif r.region_id == 'Northern Europe':
            NorthernEurope += 1
        elif r.region_id == 'Melanesia':
            Melanesia += 1
        elif r.region_id == 'Northern Africa':
            NorthernAfrica += 1
        elif r.region_id == 'Western Africa':
            WesternAfrica += 1
        elif r.region_id == 'SouthernAfrica':
            SouthernAfrica += 1
        elif r.region_id == 'Central Asia':
            CentralAsia += 1
        elif r.region_id == 'Polynesia':
            Polynesia += 1
        elif r.region_id == 'Russian Federation':
            RussianFederation += 1
        elif r.region_id == 'MiddleAfrica':
            MiddleAfrica += 1
        else:
            Micronesia += 1


    return render(request, 'chart.html', {'Asia': Asia, 'Americas': Americas, 'Europe': Europe, 'Africa': Africa,'Oceania': Oceania,'Storm':Storm,  'Flood':Flood,  'Earthquake':Earthquake,  'Wildfire':Wildfire,  'Landslide':Landslide, 'Extreme':Extreme, 'Volcanic':Volcanic,  'Drought':Drought, 'Mass':Mass, 'Glacial':Glacial, 'y1970': y1970, 'y1971': y1971, 'y1972': y1972, 'y1973': y1973, 'y1974': y1974, 'y1975': y1975, 'y1976': y1976, 'y1977': y1977, 'y1978': y1978, 'y1979': y1979, 'y1980': y1980, 'y1981': y1981, 'y1982': y1982, 'y1983': y1983, 'y1984': y1984, 'y1985': y1985, 'y1986': y1986, 'y1987': y1987, 'y1988': y1988, 'y1989': y1989, 'y1990': y1990, 'y1991': y1991, 'y1992': y1992, 'y1993': y1993, 'y1994': y1994, 'y1995': y1995, 'y1996': y1996, 'y1997': y1997, 'y1998': y1998, 'y1999': y1999, 'y2000': y2000, 'y2001': y2001, 'y2002': y2002, 'y2003': y2003, 'y2004': y2004, 'y2005': y2005, 'y2006': y2006, 'y2007': y2007, 'y2008': y2008, 'y2009': y2009, 'y2010': y2010, 'y2011': y2011, 'y2012': y2012, 'y2013': y2013, 'y2014': y2014, 'y2015': y2015, 'y2016': y2016, 'y2017': y2017, 'y2018': y2018, 'y2019': y2019, 'y2020': y2020, 'y2021': y2021, 'EasternAsia': EasternAsia, 'SouthEasternAsia': SouthEasternAsia, 'NorthernAmerica': NorthernAmerica, 'SouthernAsia': SouthernAsia, 'SouthAmerica': SouthAmerica, 'CentralAmerica': CentralAmerica, 'SouthernEurope': SouthernEurope, 'WesternEurope': WesternEurope, 'Caribbean': Caribbean, 'EasternEurope': EasternEurope, 'EasternAfrica': EasternAfrica, 'AustraliaandNewZealand': AustraliaandNewZealand, 'WesternAsia': WesternAsia, 'NorthernEurope': NorthernEurope, 'Melanesia': Melanesia, 'NorthernAfrica': NorthernAfrica, 'WesternAfrica': WesternAfrica, 'SouthernAfrica': SouthernAfrica, 'CentralAsia': CentralAsia, 'Polynesia': Polynesia, 'RussianFederation': RussianFederation, 'MiddleAfrica': MiddleAfrica, 'Micronesia': Micronesia})








