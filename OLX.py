# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 14:26:38 2019

@author: MAO
"""
#import numpy
import time 
#import requests

#from pynput.mouse import Button,Controller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# def OLX(mao,rosero)
controlador= webdriver.Chrome('Chromedriver.exe')
controlador.get('https://www.olx.com.co/')  
controlador.maximize_window()
lista = []

AYA = controlador.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/a[1]/span[1]')
AYA.click()
time.sleep(2)
controlador.execute_script("window.scrollTo(0, document.body.scrollHeight);")
resultados = controlador.find_elements_by_css_selector('li.EIR5N')
fecha = controlador.find_elements_by_css_selector('span.zLvFQ')
si = fecha[len(fecha)-1].text

#SI="HOY"
#clicks = 0
#while SI==si:
  #  controlador.find_element_by_xpath('/html/body/div/div/main/div/section/div/div/div[4]/div[2]/div/div[3]/button').click()
   # resultados = controlador.find_elements_by_css_selector('li.EIR5N')
    #fecha = controlador.find_elements_by_css_selector('span.zLvFQ')
   # fecha[len(fecha)-1].text
    #clicks += 1
    #print("Numero de clicks %d. \n " % clicks)
#print("Utilizaste %d clicks ." % clicks)
#controlador.quit()
#resultados = controlador.find_elements_by_css_selector('li.EIR5N')
#fecha = controlador.find_elements_by_css_selector('span.zLvFQ')
#for 
