# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 18:22:04 2019

@author: MAO
"""
#import time
from selenium import webdriver
import unittest
from selenium import webdriver 
#from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys 

#from selenium.common.exceptions import TimeoutException 

class SearchText(unittest.TestCase):
    def setUp(self):
        self.driver= webdriver.Chrome('Chromedriver.exe')
       # self.buscar.implicitly_wait(10)
        #self.buscar.maximize_window()
        self.driver.get("http:/www.facebook.com")
        
  #  def test_search_by_text(self):
    #    self.usuario= self.buscar.find_element_by_id("email")
     #   self.contraseña =self.buscar.find_element_by_id("pass")
      #  self.entrar = self.buscar.find_element_by_id("loginbutton")
       # self.usuario.send_keys("mauroxi94@gmail.com")
        
      #self.contraseña.send_keys("maogiant94")
       # self.entrar.submit()
        #self.nombre =self.buscar.find_element_by_name("q")
#        self.nombre.send_keys("lina acosta")
 #       self.nombre.submit()


    