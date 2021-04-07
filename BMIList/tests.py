from django.urls import resolve
from django.test import TestCase
from BMIList.views import BmiPage
from django.http import HttpRequest 

class BmiPageTest(TestCase):
  def test_root_url_resolve_to_bmipage_view(self):
   found = resolve('/')
   self.assertEqual(found.func, BmiPage)
   
  def test_bmipage_returns_correct_view(self):
   request = HttpRequest()
   response = BmiPage(request)
   html = response.content.decode('utf8')
   self.assertTrue(html.startswith ('<html>'))
   self.assertIn('<title>"BMICalculator"</title>',html)
   self.assertTrue(html.endswith ('</html>'))
   
   
   
   
   
   
   
# Create your tests here.