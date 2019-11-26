# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 11:00:16 2019

@author: MAO
"""
from selenium import webdriver 

from selenium.webdriver.common.keys import Keys 
driver = webdriver.Chrome('Chromedriver.exe')
driver.get("https://unipython.com/los-mejores-ide-python-instalar-python-os-window-linux/")
assert "Python" in driver.title
elem = driver.find_element_by_name("s")
elem.clear()
elem.send_keys("selenium")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver. close ()
