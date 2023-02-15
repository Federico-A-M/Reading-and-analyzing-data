# -*- coding: utf-8 -*-
"""
@author: feder
"""

import csv
import matplotlib.pyplot as plt
# import seaborn as sns
# sns.set()

path = "C:/Users/feder/OneDrive/Escritorio/TP"


# ¿Cuáles son los sitios que más ofertas de propiedades
# tienen? ¿esto tiene relacion con el numero de visitas?


data_zone = []
non_repeat = []
cont_repeat=0

with open(path+'/listings.csv', newline='', encoding="utf-8") as File:
    reader = csv.reader(File, delimiter=',')
    num_row = 0
    for row in reader:
        if row[5] == 'neighbourhood':
            continue # Hacemos esto para evitar leer el header
        else:
            data_zone.append(row[5])
            num_row += 1

# print(data_zone)
# print(num_row)

#armar una segunda lista con las zonas no repetidas
for element in data_zone:

    if element=="":
        continue
    else:
        if element not in non_repeat:
            non_repeat.append(element)
      
        

      
      
#Crear un diccionario con las zonas y la cantidad de publicaciones 
dicc_zonas={}        
for i in non_repeat:
    cont_repeat=0
    
    for j in data_zone:
        if j == i:
            cont_repeat +=1
            
    dicc_zonas[i] = cont_repeat




#Mostramos por pantalla el diccionario final con la cantidad de publicaciones
print(" ")            
for values, keys in dicc_zonas.items():
  print(values, keys)            
            
  
    
#ajustamos el tamaño de la imagen  
plt.figure(figsize = (15,6))
#ploteamos la grafica
plt.bar(dicc_zonas.keys(), dicc_zonas.values())
#Ajustamos el tamaño del texto y rotamos mejoramos eje x
plt.xticks(rotation = 90, fontsize=15);
plt.yticks(fontsize=20);
#Añadimos títulos y guardamos la imágen
plt.xlabel('Vecindarios',fontsize=15)
plt.ylabel('Cantidad de postulaciones',fontsize=15)
plt.title('Cantidad de ofertas por sectores en Mallorca de un Total de 17795 posteos',fontsize=20);
plt.savefig('Grafica_Barras_Mallorca.png', bbox_inches = 'tight')

    



