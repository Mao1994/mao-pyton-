# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 18:43:15 2019

@author: MAO
ESCRAPING DE DATOS 
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys 
from selenium.common.exceptions import TimeoutException 
buscar= webdriver.Chrome('Chromedriver.exe')
buscar.get("http:/www.facebook.com")
usuario= buscar.find_element_by_id("email")
contraseña =buscar.find_element_by_id("pass")
entrar = buscar.find_element_by_id("loginbutton")
usuario.send_keys("mauroxi94@gmail.com")
contraseña.send_keys("maogiant94")
entrar.click()

def ir_facebook_web(carolina,medellin):
  lista_datos = []
    try 
    WebDriverWait(buscar, 5).until(EC.presence_of_element_located((By.ID, "js_r")))
    entrar_nombre = buscar.find_element_by_id("js_r")
    entrar_nombre.send_keys(carolina)
    boton = buscar.find_element_by_id("submit")
    boton.click()