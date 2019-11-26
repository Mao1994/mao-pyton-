# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 10:30:53 2019

@author: MAO
"""
import time 
from selenium import webdriver
controlador= webdriver.Chrome('Chromedriver.exe')
controlador.get('http://newtours.demoaut.com/')
time.sleep(2)

usuario = controlador.find_element_by_xpath('/html[1]/body[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/table[1]/tbody[1]/tr[4]/td[1]/table[1]/tbody[1]/tr[1]/td[2]/table[1]/tbody[1]/tr[2]/td[3]/form[1]/table[1]/tbody[1]/tr[4]/td[1]/table[1]/tbody[1]/tr[2]/td[2]/input[1]')
contraseña = controlador.find_element_by_xpath('/html[1]/body[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/table[1]/tbody[1]/tr[4]/td[1]/table[1]/tbody[1]/tr[1]/td[2]/table[1]/tbody[1]/tr[2]/td[3]/form[1]/table[1]/tbody[1]/tr[4]/td[1]/table[1]/tbody[1]/tr[3]/td[2]/input[1]')
boton = controlador.find_element_by_name('login')
usuario.send_keys('hola')
contraseña.send_keys('puto el que lo lea')
boton.click()
time.sleep(2)
link_de_registro = controlador.find_element_by_link_text('registration form')
assert link_de_registro.text =='registration form'
print('pase por aqui care mondiuu')
assert link_de_registro.tag_name =='a'
controlador.quit()