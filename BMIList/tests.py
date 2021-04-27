#from django.urls import resolve
from BMIList.models import Item
from django.test import TestCase
#from BMIList.views import BMIPage
#from django.http import HttpRequest 
class BmiPageTest(TestCase):

    def test_bmipage_returns_correct_view(self):
        response = self.client.get ('/')
        self.assertTemplateUsed(response,'bmi.html')
        
    def test_save_post_request(self):
        response = self.client.post('/', data={'age':'Age'})
        self.assertIn('Age', response.content.decode())
        self.assertTemplateUsed(response,'bmi.html')
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
        
    '''def test_uses_mainpage_template(self):
        response = self.client.get ('/')
        self.assertTemplateUsed(response,'bmi.html')'''
        
    
         
    '''def test_bmipage_returns_correct_view(self):
        response = self.client.get('/')
        html = response.content.decode('utf8')
        string_html = render_to_string('bmi.html')
        self.assertEqual(html,string_html)
        self.assertTemplateUsed(response,'bmi.html')'''


  #def test_root_url_resolve_to_bmipage_view(self):
   #found = resolve('/')
   #self.assertEqual(found.func, BmiPage)

