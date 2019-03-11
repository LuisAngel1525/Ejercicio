from bs4 import BeautifulSoup
import urllib3
import pandas as pd
from tabulate import tabulate
import requests
import re
from numpy import array
http=urllib3.PoolManager()

urllib3.disable_warnings()

url='https://es.wikipedia.org/wiki/Anexo:Presidentes_de_los_Estados_Unidos_por_edad'
#url='https://es.wikipedia.org/wiki/Anexo:Gobernantes_de_M%C3%A9xico_por_edad'
responde=requests.get(url).text


soup=BeautifulSoup(responde, "html.parser")
tabla = soup.find('table')
listaNombres =[] #Guarda los nombres
listaEdades = [] #Guarda las edades
porcendias=0;
name=""
price=""
Fila=0
filas = tabla.find_all('tr')
countarre=0
for fila in filas:
    if Fila==1:
        nroCelda=0
        for celda in fila.find_all('td'):
            if nroCelda==1:
                name=celda.getText()
                listaNombres.append(name)
               # print("Precidente:", name)
            if nroCelda==4:
                price=celda.getText()
                price = re.sub("\D","",price)
                anio= price[:2]
                porcen= price[2:]
                porcdias = int (porcen)/365
                edadDecimal = int(anio)+porcdias
                print("Precidente:", name,"Edad:", edadDecimal, "\n")
                listaEdades.append(edadDecimal)
            nroCelda=nroCelda+1
    else:
        Fila=Fila+1

