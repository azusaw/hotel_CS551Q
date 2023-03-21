from django.test import Client, TestCase
from django.urls import reverse
from django.utils import timezone
from ..models import Disaster, Type, Region, Continent
from ..forms import SearchConditionForm

class FormTest(TestCase):

    fixtures = ['disaster.json']

    def setUp(self):
        self.types = ['All'] + [t.id for t in Type.objects.all()]
        self.continents = ['All'] + [c.id for c in Continent.objects.all()]
        self.regions = ['All'] + [r.id for r in Region.objects.all()]

    def test_valid_form(self):
        data = {
            'country': 'Bangladesh',
            'continent': 'Asia',
            'region': 'SouthernAsia',
            'type': 'Flood',
            'order': 'totalDeaths'
        }
        form = SearchConditionForm(data=data)
        self.assertTrue(form.is_valid())







