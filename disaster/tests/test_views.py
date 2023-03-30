from django.test import TestCase, Client
from django.urls import reverse
from ..models import Disaster, Type, Region, Continent

class DisasterViewsTest(TestCase):

    fixtures = ['disaster.json']

    # test the home page
    # 1
    def test_home(self):
        client = Client()
        response = client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, "Disasters in the world 1970 - 2021")

    # 2
    def test_views_home_use_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'home.html')

    # test the all page
    # 3
    def test_disaster_list(self):
        client = Client()
        response = client.get('/all')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "2020-0055-WEF")
        self.assertContains(response, "500")
        self.assertContains(response, "Asia")

    # 4
    def test_views_all_use_correct_template(self):
        response = self.client.get(reverse('all'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'all.html')

    # test the disaster_detail page
    # 5
    def test_disaster_detail(self):
        client = Client()
        response = client.get('/detail/2020-0055-WEF/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "2020-0055-WEF")
        self.assertContains(response, "90000")
        self.assertContains(response, "7876")

    # test the search page
    # 6
    def test_search(self):
        client = Client()
        response = client.get('/search')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search.html')
        self.assertContains(response, "Search Data by Conditions")


    # 7
    def test_views_serch_use_correct_template(self):
        response = self.client.get(reverse('search'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'search.html')

    # 8
    def test_new(self):
        client = Client()
        response = client.get('/new')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'disaster_edit.html')
        self.assertContains(response, "Edit:")

