from django import forms

from .models import Type, Continent, Region, Disaster


class DisasterForm(forms.ModelForm):
    """ Form used for search conditions in /new /edit page """

    class Meta:
        model = Disaster
        fields = '__all__'

    # Get options from database
    types = Type.objects.all()
    continents = Continent.objects.all()
    regions = Region.objects.all()

    disasterNo = forms.CharField(
        widget=forms.widgets.TextInput(attrs={'class': 'form-control col-sm-5'})
    )
    year = forms.CharField(
        widget=forms.widgets.NumberInput(attrs={'class': 'form-control col-sm-5'})
    )
    seq = forms.CharField(
        widget=forms.widgets.TextInput(attrs={'class': 'form-control col-sm-5'})
    )
    group = forms.CharField(
        widget=forms.widgets.TextInput(attrs={'class': 'form-control col-sm-5'})
    )
    subgroup = forms.CharField(
        widget=forms.widgets.TextInput(attrs={'class': 'form-control col-sm-5'})
    )
    type = forms.fields.ChoiceField(
        required=False,
        choices=[('', 'All')] + [(item.id, item.id) for item in types],
        widget=forms.widgets.Select(attrs={'class': 'form-control form-inline'})
    )
    subtype = forms.CharField(
        required=False,
        widget=forms.widgets.TextInput(attrs={'class': 'form-control col-sm-5'})
    )
    eventName = forms.CharField(
        required=False,
        widget=forms.widgets.TextInput(attrs={'class': 'form-control col-sm-5'})
    )
    iso = forms.CharField(
        required=False,
        widget=forms.widgets.TextInput(attrs={'class': 'form-control col-sm-5'})
    )
    region = forms.fields.ChoiceField(
        required=False,
        choices=[('', 'All')] + [(item.id, item.id) for item in regions],
        widget=forms.widgets.Select(attrs={'class': 'form-control col-sm-5'})
    )
    continent = forms.fields.ChoiceField(
        required=False,
        choices=[('', 'All')] + [(item.id, item.id) for item in continents],
        widget=forms.widgets.Select(attrs={'class': 'form-control col-sm-5'})
    )
    country = forms.CharField(
        required=False,
        widget=forms.widgets.TextInput(attrs={'class': 'form-control col-sm-5'})
    )
    location = forms.CharField(
        required=False,
        widget=forms.widgets.TextInput(attrs={'class': 'form-control col-sm-5'})
    )
    startYear = forms.CharField(
        required=False,
        widget=forms.widgets.NumberInput(attrs={'class': 'form-control col-sm-5'})
    )
    startMonth = forms.CharField(
        required=False,
        widget=forms.widgets.NumberInput(attrs={'class': 'form-control col-sm-5'})
    )
    startDay = forms.CharField(
        required=False,
        widget=forms.widgets.NumberInput(attrs={'class': 'form-control col-sm-5'})
    )
    endYear = forms.CharField(
        required=False,
        widget=forms.widgets.NumberInput(attrs={'class': 'form-control col-sm-5'})
    )
    endMonth = forms.CharField(
        required=False,
        widget=forms.widgets.NumberInput(attrs={'class': 'form-control col-sm-5'})
    )
    endDay = forms.CharField(
        required=False,
        widget=forms.widgets.NumberInput(attrs={'class': 'form-control col-sm-5'})
    )
    totalDeath = forms.CharField(
        required=False,
        widget=forms.widgets.NumberInput(attrs={'class': 'form-control col-sm-5'})
    )
    injured = forms.CharField(
        required=False,
        widget=forms.widgets.NumberInput(attrs={'class': 'form-control col-sm-5'})
    )
    affected = forms.CharField(
        required=False,
        widget=forms.widgets.NumberInput(attrs={'class': 'form-control col-sm-5'})
    )
    totalAffected = forms.CharField(
        required=False,
        widget=forms.widgets.NumberInput(attrs={'class': 'form-control col-sm-5'})
    )
    totalDeaths = forms.CharField(
        required=False,
        widget=forms.widgets.NumberInput(attrs={'class': 'form-control col-sm-5'})
    )
    homeless = forms.CharField(
        required=False,
        widget=forms.widgets.NumberInput(attrs={'class': 'form-control col-sm-5'})
    )
    damageCost = forms.CharField(
        required=False,
        widget=forms.widgets.NumberInput(attrs={'class': 'form-control col-sm-5'})
    )


class SearchConditionForm(forms.Form):
    """ Form used for search conditions in /search page """
    types = Type.objects.all()
    continents = Continent.objects.all()
    regions = Region.objects.all()

    country = forms.CharField(
        required=False,
        widget=forms.widgets.TextInput(attrs={'class': 'form-control col-sm-5'})
    )
    continent = forms.fields.ChoiceField(
        required=False,
        choices=[('', 'All')] + [(item.id, item.id) for item in continents],
        widget=forms.widgets.Select(attrs={'class': 'form-control col-sm-5'})
    )
    region = forms.fields.ChoiceField(
        required=False,
        choices=[('', 'All')] + [(item.id, item.id) for item in regions],
        widget=forms.widgets.Select(attrs={'class': 'form-control col-sm-5'})
    )
    type = forms.fields.ChoiceField(
        required=False,
        choices=[('', 'All')] + [(item.id, item.id) for item in types],
        widget=forms.widgets.Select(attrs={'class': 'form-control form-inline'})
    )
    order = forms.fields.ChoiceField(
        required=False,
        choices=[
            ('year', ' Year - Asc'),
            ('-year', ' Year - Desc'),
            ('totalDeaths', ' TotalDeaths - Asc'),
            ('-totalDeaths', ' TotalDeaths - Desc'),
            ('damageCost', ' damageCost - Asc'),
            ('-damageCost', ' damageCost - Desc')
        ],
        widget=forms.widgets.Select(attrs={'class': 'form-control form-inline'})
    )
