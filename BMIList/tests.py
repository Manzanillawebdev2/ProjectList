#from django.urls import resolve
from BMIList.models import Item
from django.test import TestCase
from BMIList.views import BmiPage
#from django.http import HttpRequest 
class BmiPageTest(TestCase):
	def test_uses_template(self):
		response = self.client.get ('/')
		self.assertTemplateUsed(response,'bmi.html')
	
	def test_save_only_if_necessary(self):
		response = self.client.get ('/')
		self.assertEqual(Item.objects.count(), 0)
	
	def test_at_request(self):
		response = self.client.post('/', data={'age':'Age'})
#		self.assertIn('age', response.content.decode())
#		self.assertTemplateUsed(response,'bmi.html')
		
		self.assertEqual(Item.objects.count(), 1)
		newItem = Item.objects.first()
		self.assertEqual(newItem.text, 'Age')
		
	def test_palit_POST(self):
		response = self.client.post('/', data={'age':'age'})
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response['location'], '/BMIList/mgm_url/')
		
	def test_template_display_items(self):
	        Item.objects.create(text= 'mgm1')
	        Item.objects.create(text= 'mgm2')
	        response = self.client.get('/')
	        self.assertIn('mgm1', response.content.decode())
	        self.assertIn('mgm2', response.content.decode())



class ORMTest(TestCase):

	def test_saveretrievelist(self):
		txtItem1=Item()
		txtItem1.text='item one'
		txtItem1.save()
		txtItem2=Item()
		txtItem2.text='item two'
		txtItem2.save()
		saved_Items=Item.objects.all()
		self.assertEqual(saved_Items.count(),2)
		savedItem1=saved_Items[0]
		savedItem2=saved_Items[1]
		self.assertEqual(savedItem1.text, 'item one')
		self.assertEqual(savedItem2.text, 'item two')
		
	
class ViewTest(TestCase):
	def test_displays_all(self):
		Item.objects.create(text='Gelyn')
		Item.objects.create(text='Danielle')
		response = self.client.get('/BMIList/mgm_url/')
		self.assertContains(response,'Gelyn')
		self.assertContains(response,'Danielle')
		


