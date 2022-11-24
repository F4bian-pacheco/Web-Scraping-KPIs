from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import re
from time import gmtime, strftime


service = Service('/usr/bin/geckodriver')

webdriver = webdriver.Firefox(service=service)

df = pd.read_csv("modelos_a1.csv")
df_regiones = pd.read_csv("regiones.csv")
# marcas = df["marcas"].tolist()
# modelos = df["modelos"].tolist()
regiones = df_regiones["Regiones"].tolist()

# from df to tuple
df = df.to_records(index=False).tolist()


for marca, modelo in df:
    data_modelo = modelo.lower().replace(" ", "-")
    for region in regiones:
        url = 'https://www.chileautos.cl/vehiculos/autos-veh%C3%ADculo/usado-tipo/' + \
            marca.lower()+'/'+data_modelo+'/'+region.lower()+'/'
        webdriver.get(url)
        webdriver.maximize_window()
        webdriver.implicitly_wait(5)

        # anuncio = webdriver.element_to_be_clickable(
        #     (By.XPATH, "/html/body/div/div[1]/div/div[1]/div[2]/svg"))
        # anuncio.click()

        num_publicaciones = webdriver.find_element(
            By.TAG_NAME, "h1")
        num_publicaciones = num_publicaciones.text.split(" ")[0]
        # num_publicaciones = "258"
        if int(num_publicaciones) > 12:
            num_p = int(num_publicaciones)//12
            rango = range(num_p+1)
        else:
            rango = range(1)
        j = 1
        for i in rango:

            url_2 = 'https://www.chileautos.cl/vehiculos/autos-veh%C3%ADculo/usado-tipo/' + \
                marca.lower()+'/'+data_modelo+'/'+region.lower()+'/?offset='+str(12*i)
            webdriver.get(url_2)
            webdriver.maximize_window()
            webdriver.implicitly_wait(5)
            lista_publicaciones = webdriver.find_elements(
                By.CLASS_NAME, "listing-item")
            for publicacion in lista_publicaciones:
                texto = publicacion.find_element(
                    By.CLASS_NAME, "card-body")
                lista = texto.text.split("\n")

                titulo = lista[0].split(" ")
                precio = lista[2]
                kilometraje = lista[3]
                try:
                    combustible = lista[5]
                except:
                    combustible = "N/A"

                p = re.compile('.*([1-2][0-9]{3})')
                anio = [s for s in titulo if p.match(s)]
                if len(anio) == 0:
                    anio = "N/A"
                else:
                    anio = anio[0]
                print(j, marca, modelo, region, anio,
                      precio, kilometraje, combustible)
                j += 1
                data_dict = {"marcas": [], "modelos": [], "regiones": [],
                             "precios": [], "año": [], "kilometraje": [], "combustible": []}
                data_dict["marcas"].append(marca)
                data_dict["modelos"].append(modelo)
                data_dict["regiones"].append(region)
                data_dict["precios"].append(precio)
                data_dict["año"].append(anio)
                data_dict["kilometraje"].append(kilometraje)
                data_dict["combustible"].append(combustible)
                df_data = pd.DataFrame(data_dict)
                df_data.to_csv("data_a1.csv", mode="a",
                               index=False, header=False)

# print(df_data.head())
strftime("%Y-%m-%d %H:%M:%S", gmtime())
# titulo = webdriver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[1]/div[3]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[1]/h3/a")
# print(titulo.text)
