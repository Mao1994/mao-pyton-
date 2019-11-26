# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 11:49:11 2019

@author: MAO
"""

import time 
import unittest
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
class PytonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('Chromedriver.exe')
    def test_search_in_python_org(self):
        driver =self.driver
        driver.get("https://unipython.com/los-mejores-ide-python-instalar-python-os-window-linux/")
        time.sleep(3)
        self.assertIn("Pytthon",driver.title)
        time.sleep(3)
        elem = driver.find_element_by_name("s")
        time.sleep(3)
        elem.send_keys("aprender")
        elem.send_keys(Keys.RETURN)
        time.sleep(3)
        assert "No results found." not in driver.page_source
    def tearDown(self):
        self.driver.close()
if __name__ == "__main__":
                   unittest.main()

#class PytonOrgSearch(unittest.testcase):