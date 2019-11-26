# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 11:37:22 2019

@author: MAO
"""

from selenium import webdriver
from selenium.webdriver.support.ui import Select

    
import unittest
import time 
class newTours(unittest.TestCase):
    def setUp(self):
        self.controlador = webdriver.Chrome('Chromedriver.exe')
        self.controlador.get('http://newtours.demoaut.com/')
        self.controlador.current_url
        time.sleep(2)
        
    def test_desplegable(self):
        self.controlador.find_element_by_link_text('REGISTER').click()
        D_pais = Select(self.controlador.find_element_by_name('country'))
        D_pais.select_by_index(5)
        D_pais.select_by_value('11')
        D_pais.select_by_visible_text('COLOMBIA')
        self.assertEquals(D_pais.first_selected_option.text.strip(),'COLOMBIA')
        
    def tearDown(self):
        self.controlador.quit()
