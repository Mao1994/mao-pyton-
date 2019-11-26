# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 12:24:34 2019
@author: MAO
"""
import time 
import selenium
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

usuario ="mauroxi94@gmail.com"
contraseña = "maogiant94"

driver.get("https://www.facebook.com/")
assert ("Facebook") in driver.title
nombre = driver.find_element_by_id("email")
nombre.send_keys(usuario)
pasword = driver.find_element_by_id("pass")
pasword.send_keys(contraseña)
pasword.submit()
nombre = driver.find_element_by_class_name("_1frb")
nombre.send_keys("#unalmed")
nombre.submit()


cheese = driver.find_element_by_class_name("_4xj-")
