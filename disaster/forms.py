from django import forms

from .models import Type, Continent, Region


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
