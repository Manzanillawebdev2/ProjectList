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
	   
	#def tearDown(self):
	   #self.browser.quit()
	def check_rows_in_list_table(self, row_text):
	   table = self.browser.find_element_by_id('tableko')
	   rows = table.find_elements_by_tag_name('tr')
	   self.assertIn(row_text, [row.text for row in rows]) 
	   
	def test_start_list_and_retrieve_it(self):
           self.browser.get('http://localhost:8000')
           self.assertIn('"BMICalculator"', self.browser.title)
           headerText = self.browser.find_element_by_tag_name('h1').text
           self.assertIn('Body Mass Index Calculator', headerText)
           inputname1 = self.browser.find_element_by_id('name')
           self.assertEqual(inputname1.get_attribute('Placeholder'),'type your name here')
           inputname1.send_keys('Milleth')
           inputage1 = self.browser.find_element_by_id('age')
           inputheight1 = self.browser.find_element_by_id('height')
           inputweight1 = self.browser.find_element_by_id('weight')
           inputgender1 = self.browser.find_element_by_id('gender')
           btnenter = self.browser.find_element_by_id('enter')
           self.assertEqual(inputage1.get_attribute('placeholder'),'type your age')
           self.assertEqual(inputgender1.get_attribute('placeholder'),'male or female')
           self.assertEqual(inputheight1.get_attribute('placeholder'),'what is your height (in cm)?')
           self.assertEqual(inputweight1.get_attribute('placeholder'),'what is your weight (in kg)?')
    
           time.sleep(1)
           inputage1.send_keys('21')
           time.sleep(1)
           inputgender1.send_keys('female')
           time.sleep(1)
           inputheight1.send_keys('156')
           time.sleep(1)
           inputweight1.send_keys('42')
           time.sleep(1)
           btnenter.click()
           time.sleep(1)
           self.check_rows_in_list_table('1: 21')
           
#This page should update and show the name of the list
           inputage1 = self.browser.find_element_by_id('age')
           inputgender1 = self.browser.find_element_by_id('gender')
           inputheight1 = self.browser.find_element_by_id('height')
           inputweight1 = self.browser.find_element_by_id('weight')
           btnenter = self.browser.find_element_by_id('enter')
           self.assertEqual(inputage1.get_attribute('placeholder'),'type your age')
           self.assertEqual(inputgender1.get_attribute('placeholder'),'male or female')
           self.assertEqual(inputheight1.get_attribute('placeholder'),'what is your height (in cm)?')
           self.assertEqual(inputweight1.get_attribute('placeholder'),'what is your weight (in kg)?')
           time.sleep(1)
    
           time.sleep(1)
           inputage1.send_keys('18')
           time.sleep(1)
           inputgender1.send_keys('male')
           time.sleep(1)
           inputheight1.send_keys('155')
           time.sleep(1)
           inputweight1.send_keys('50')
           time.sleep(1)
           btnenter.click()
           time.sleep(1)
           self.check_rows_in_list_table('2: 18')
'''           table = self.browser.find_element_by_id('tableko')
           rows = table.find_elements_by_tag_name('tr')
           self.assertIn('21 156 42',[row.text for row in rows])
	   #self.fail('Finish the test NOW!!!????')'''
	   
	   
if __name__== '__main__':
   unittest.main(warnings='ignore')
