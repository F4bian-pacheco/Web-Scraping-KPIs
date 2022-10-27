from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd


webdriver = webdriver.Firefox(executable_path='/usr/bin/geckodriver')

webdriver.get('https://www.chileautos.cl/vehiculos/autos-veh%C3%ADculo/')
webdriver.implicitly_wait(10)

# Get title
print(webdriver.title)
