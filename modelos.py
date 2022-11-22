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

    modelo_filter = webdriver.find_element(
        By.XPATH, "/html/body/div[2]/div[3]/div[1]/div[1]/div[3]/div[1]/section/div[2]/div/div[2]/div[4]/div[3]/div/div/ul[1]/li/div[2]/div")
    modelo_filter.click()
    modelos = webdriver.find_element(By.CLASS_NAME, "multiselect-facets")
    modelos = modelos.find_elements(By.CLASS_NAME, "multiselect-facets-item")
    for modelo in modelos:
        list_modelo = modelo.text.split("\n")
        if list_modelo[0] not in modelos_dict["modelos"]:
            modelos_dict["marcas"].append(marca)
            modelos_dict["modelos"].append(list_modelo[0])

df_modelos = pd.DataFrame(modelos_dict)
print(df_modelos.head())
df_modelos.to_csv("modelos.csv", index=False)
