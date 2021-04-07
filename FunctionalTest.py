#from selenium import webdriver
#browser = webdriver.Firefox()
#browser.get('http://127.0.0.1:8000')

from selenium import webdriver
import unittest

from selenium.webdriver.common.keys import Keys
import time




class PageTest(unittest.TestCase):

	def setUp(self):
	   self.browser = webdriver.Firefox()
	   
	def tearDown(self):
	   self.browser.quit()
	   
	def test_start_list_and_retrieve_it(self):
           self.browser.get('http://localhost:8000')
           self.assertIn('"BMICalculator"', self.browser.title)
           headerText = self.browser.find_element_by_tag_name('h1').text
           self.assertIn('Body Mass Index Calculator', headerText)
           inputheight1 = self.browser.find_element_by_id('height')
           inputweight1 = self.browser.find_element_by_id('weight')
           btnenter = self.browser.find_element_by_id('enter')
           self.assertEqual(inputheight1.get_attribute('placeholder'),'what is your height (in inches)?')
           self.assertEqual(inputweight1.get_attribute('placeholder'),'what is your weight (in kg)?')
           time.sleep(2)
           inputheight1.send_keys('156')
           time.sleep(2)
           inputweight1.send_keys('42')
           time.sleep(2)
           btnenter.click()
           time.sleep(1)
	   #self.fail('Finish the test NOW!!!????')
	   
	   
if __name__== '__main__':
   unittest.main(warnings='ignore')
