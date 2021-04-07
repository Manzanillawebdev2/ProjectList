from django.urls import resolve
from django.test import TestCase
from BMIList.views import BmiPage

class BmiPageTest(TestCase):
  def test_root_url_resolve_to_bmipage_view(self):
   found = resolve('/')
   self.assertEqual(found.func, BmiPage)
# Create your tests here.
