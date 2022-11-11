from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd


service = Service('/usr/bin/geckodriver')

webdriver = webdriver.Firefox(service=service)

webdriver.get('https://www.chileautos.cl/vehiculos/autos-veh%C3%ADculo/')
webdriver.maximize_window()
webdriver.implicitly_wait(5)

# elementos_filter = webdriver.find_element(By.CLASS_NAME, 'nav-element')
marca_filter = webdriver.find_element(
    By.XPATH, "//div[@data-name='marca']")

marca_filter.click()
# wait for the element to be visible

marcas = webdriver.find_element(By.CLASS_NAME, "multiselect-facets")
marcas = marcas.find_elements(By.CLASS_NAME, "multiselect-facets-item")
marcas_dict = {"marcas": []}
for marca in marcas:
    list_marca = marca.text.split("\n")
    marcas_dict["marcas"].append(list_marca[0])

df = pd.DataFrame(marcas_dict)
df.to_csv("marcas.csv", index=False)

print(df)
# Get title
print(webdriver.title)
