from django.test import TestCase, Client
from django.urls import reverse
from ..models import Disaster, Type, Region, Continent

class DisasterViewsTest(TestCase):

    fixtures = ['disaster.json']

    # test the home page
    def test_home(self):
        client = Client()
        response = client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, "Disasters in the world 1970 - 2021")

    def test_views_home_use_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'home.html')

    # test the all page
    def test_disaster_list(self):
        client = Client()
        response = client.get('/all')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "2020-0055-WEF")
        self.assertContains(response, "500")
        self.assertContains(response, "Asia")

    def test_views_all_use_correct_template(self):
        response = self.client.get(reverse('all'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'all.html')

    # test the disaster_detail page
    def test_disaster_detail(self):
        client = Client()
        response = client.get('/detail/2020-0055-WEF/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "2020-0055-WEF")
        self.assertContains(response, "90000")
        self.assertContains(response, "7876")

    # test the search page
    def test_search(self):
        client = Client()
        response = client.get('/search')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search.html')
        self.assertContains(response, "Search Data by Conditions")

    def test_views_serch_use_correct_template(self):
        response = self.client.get(reverse('search'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'search.html')
    