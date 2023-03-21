from django.test import Client, TestCase
from ..models import Disaster, Continent, Region, Type

class DisasterModelTest(TestCase):

    fixtures = ['disaster.json']

    def test_disaster(self):
        disaster = Disaster.objects.get(disasterNo="2020-0055-WEF")
        self.assertEqual(disaster.year, 2020)
        disasters =Disaster.objects.all()
        self.assertEqual(disasters.count(), 1)

    def test_continent(self):
        continent = Continent.objects.get(pk="Asia")
        self.assertEqual(continent.id, "Asia")
        continents =Continent.objects.all()
        self.assertEqual(continents.count(), 1)

    def test_region(self):
        region = Region.objects.get(pk="SouthernAsia")
        self.assertEqual(region.continent.id, "Asia") # assert continent object
        regions = Region.objects.all()
        self.assertEqual(regions.count(), 1)

    def test_type(self):
        disaster_type = Type.objects.get(pk="Flood")
        self.assertEqual(disaster_type.id, "Flood")
        types = Type.objects.all()
        self.assertEqual(types.count(), 1)

