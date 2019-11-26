# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 14:13:10 2019

@author: MAO
"""

import time 
import selenium
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

#usuario ="mauroxi94@gmail.com"
#contraseña = "maogiant94"
driver = webdriver.Chrome('Chromedriver.exe')
driver.maximize_window()
driver.get("https://www.youtube.com")
print(driver.title)
driver.back()
driver.forward()


#assert ("Facebook") in driver.title
#nombre = driver.find_element_by_id("email")
#nombre.send_keys(usuario)
#pasword = driver.find_element_by_id("pass")
#pasword.send_keys(contraseña)
#pasword.submit()x
#nombre = driver.find_element_by_id("search")
#nombre.send_keys("gerardo moran")
#nombre = driver.find_element_by_id("search-icon-legacy")
#nombre.click()