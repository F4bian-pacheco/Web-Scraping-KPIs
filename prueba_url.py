from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd


service = Service('/usr/bin/geckodriver')

webdriver = webdriver.Firefox(service=service)

df = pd.read_csv("marcas.csv")
marcas = df["marcas"].tolist()

modelos_dict = {"marcas": [], "modelos": []}
for marca in marcas:
    webdriver.get(
        'https://www.chileautos.cl/vehiculos/autos-veh%C3%ADculo/'+marca.lower()+'/')
    webdriver.maximize_window()
    webdriver.implicitly_wait(5)
    break
