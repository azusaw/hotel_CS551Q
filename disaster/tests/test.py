from django.test import TestCase
from ..models import Disaster, Continent, Region, Type

class DisasterModelTest(TestCase):

    def setUp(self):
        self.continent = Continent.objects.create(id='test_continent')
        self.region = Region.objects.create(id='test_region', continent=self.continent)
        self.type = Type.objects.create(id='test_type')
        self.disaster = Disaster.objects.create(
            disasterNo='test_disaster',
            year=2023,
            seq=1,
            group='test_group',
            subgroup='test_subgroup',
            type=self.type,
            eventName='test_eventName',
            country='test_country',
            iso='test_iso',
            region=self.region,
            continent=self.continent,
            location='test_location',
            startYear=2023,
            startMonth=3,
            startDay=27,
            endYear=2023,
            endMonth=3,
            endDay=27,
            totalDeaths=0,
            injured=0,
            affected=0,
            totalAffected=0,
            homeless=0,
            damageCost=0
        )

    def test_disaster_creation(self):
        self.assertEqual(self.disaster.disasterNo, 'test_disaster')
        self.assertEqual(self.disaster.year, 2023)
        self.assertEqual(self.disaster.seq, 1)
        self.assertEqual(self.disaster.group, 'test_group')
        self.assertEqual(self.disaster.subgroup, 'test_subgroup')
        self.assertEqual(self.disaster.type, self.type)
        self.assertEqual(self.disaster.eventName, 'test_eventName')
        self.assertEqual(self.disaster.country, 'test_country')
        self.assertEqual(self.disaster.iso, 'test_iso')
        self.assertEqual(self.disaster.region, self.region)
        self.assertEqual(self.disaster.continent, self.continent)
        self.assertEqual(self.disaster.location, 'test_location')
        self.assertEqual(self.disaster.startYear, 2023)
        self.assertEqual(self.disaster.startMonth, 3)
        self.assertEqual(self.disaster.startDay, 27)
        self.assertEqual(self.disaster.endYear, 2023)
        self.assertEqual(self.disaster.endMonth, 3)
        self.assertEqual(self.disaster.endDay, 27)
        self.assertEqual(self.disaster.totalDeaths, 0)
        self.assertEqual(self.disaster.injured, 0)
        self.assertEqual(self.disaster.affected, 0)
        self.assertEqual(self.disaster.totalAffected, 0)
        self.assertEqual(self.disaster.homeless, 0)
        self.assertEqual(self.disaster.damageCost, 0)
