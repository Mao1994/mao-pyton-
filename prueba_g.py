# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 12:32:45 2019

@author: MAO
"""
import unittest
from selenium import webdriver

class SearchText(unittest.TestCase):
  def setUp(self):
    # crea la nueva seccion del nagegador
    self.driver = webdriver.Chrome('Chromedriver.exe')
    self.driver.implicitly_wait(30)
    self.driver.maximize_window()
    # navega hasta la url
    self.driver.get("http://www.google.com/")

  def test_search_by_text(self):
    # obtener el cuadro de texto de búsqueda
    self.search_field = self.driver.find_element_by_name("q")

    # escribe la palabra clave de búsqueda y la envía
    self.search_field.send_keys("aprender python")
    self.search_field.submit()

    #obtener la lista de elementos que se muestran después de la búsqueda
    #actualmente en la página de resultados usando find_elements_by_class_namemethod

    lists = self.driver.find_elements_by_class_name("r")
    no=len(lists)
    self.assertEqual(10, len(lists))