#!/usr/bin/env python
# coding: utf-8

# # función de lectura csv

# In[11]:


import csv


# In[12]:


def leer_csv(path : str) -> list:
    """
    Leer un archivo csv.
    """
    datos = []
    encabezados = []
    primera_iteracion = True
    with open(path, newline="", encoding="utf-8") as File:
        reader = csv.reader(File, delimiter=",")
        for fila in reader:
            if primera_iteracion:
                encabezados = fila.copy()
                primera_iteracion = False
            else:
                dato = {}
                for i, encabezado in enumerate(encabezados):
                    dato[encabezado] = fila[i]
                datos.append(dato)
                
        File.close()
    return datos


# ### A continuación se presentan las 4 funciones empleadas

# In[2]:


'''
@Author Simón Revello.
Pregunta: Retorna una lista de diccionarios donde la key es el vecindario y el valor es el promedio.
'''
def precio_prom_por_vecindario(datos: list) -> list:

    precios_vecindarios = {}
    cant_vecindarios = {}
    precios_promedios = {}
    for dato in datos:
        nombre_vecindario = dato["neighbourhood"]
        if nombre_vecindario in precios_vecindarios:
            precios_vecindarios[nombre_vecindario] += float(dato["price"])
            cant_vecindarios[nombre_vecindario] += 1
        else:
            print(dato)
            precios_vecindarios[nombre_vecindario] = float(dato["price"])
            cant_vecindarios[nombre_vecindario] = 1
    for nom_vecindario in precios_vecindarios:
        precios_promedios[nom_vecindario] = precios_vecindarios[nom_vecindario] / cant_vecindarios[nom_vecindario]
    return precios_promedios


# In[14]:


'''
@Author: Marien B.
Pregunta: ¿Cuál es el precio promedio dependiendo el tipo de habitación 
(casas, departamentos, habitaciones compartidas, hoteles)?
'''

def diferent_room_types(data):
    casas_departamentos = [] 
    habitacion_privada = []    
    habitacion_compartida = []  
    hotel = []               

    room_type={} #dicccionario para guardar precios por tipo de habitacion
    
    for row in data:
        if row["room_type"] == 'Entire home/apt': # para evitar leer datos erroneos
            casas_departamentos = row["room_type"]#guardamos el tipo de habitacion
            p = float(row["price"])#guardamos el precio en una variable
            
            if casas_departamentos in room_type.keys():#guardamos la key
                room_type[casas_departamentos].append(p)#si ya existe agregamos el precio
            else: #sino crear arreglo
                room_type[casas_departamentos] = [p]
            
        elif row["room_type"] == 'Private room':
            habitacion_privada = row["room_type"]
            p = float(row["price"])
                
            if habitacion_privada in room_type.keys():
                room_type[habitacion_privada].append(p)
            else:
                room_type[habitacion_privada] = [p] 
            
        elif row["room_type"] == 'Shared room': 
            habitacion_compartida = row["room_type"] 
            p = float(row["price"])
                
            if habitacion_compartida in room_type.keys():
                room_type[habitacion_compartida].append(p)
            else:
                room_type[habitacion_compartida] = [p]          
            
        elif row["room_type"] == 'Hotel room':
            hotel = row["room_type"]
            p = float(row["price"])
                
            if hotel in room_type.keys():
                room_type[hotel].append(p)
            else:
                room_type[hotel] = [p]


    precio_medio_segun_habitacion = {} # Creo un diccionario donde guardar el promedio

    for types, precio in room_type.items():
        precio_medio_segun_habitacion[types] = precio_promedio(precio)

    return precio_medio_segun_habitacion



def precio_promedio(precio): # creo una funcion donde calculo el promedio por habitacion
    return sum(precio)/len(precio)


# In[15]:


'''
@Author: Federico A. Martín
Pregunta: ¿Cuáles son los barrios que más ofertas de propiedades tienen?
'''
def ofertas_por_barrio(data):

    data_zone = []
    non_repeat = []
    cont_repeat=0

    for row in data:
        data_zone.append(row["neighbourhood"])


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

    return dicc_zonas



# In[16]:


'''
@Author: Julián F. Britos
Pregunta: A partir de los barrios con más postulaciones: ¿Cuál es la distribución de precios en cada uno?
'''
def dist_de_precios_segun_el_barrio(data, dicc_zonas):
    # Ordenamiento del diccionario de mayor a menor valor (postulaciones)
    dicc_zonas_ord = sorted(dicc_zonas.items(), key=lambda x: x[1], reverse=True)

    # Guardado de los 3 barrios con mas postulaciones
    cont = 0
    barrios = []

    for nombre  in dicc_zonas_ord: 
        if cont < 3:
            barrio = {
                "nombre": nombre[0]
            }
            barrios.append(barrio) 
        else:
            break 
        cont += 1

    # Listas de lugares por cada barrio
    barrio1 = []
    barrio2 = []
    barrio3 = []

    for row in data:
        # Si la posicion 5 de la fila, es decir el barrio, es igual al nombre del barrio se agrega a la lista 
        if row["neighbourhood"] == barrios[0]['nombre']:
            barrio1.append(float(row["price"]))
        elif row["neighbourhood"] == barrios[1]['nombre']:
            barrio2.append(float(row["price"]))
        elif row["neighbourhood"] == barrios[2]['nombre']:
            barrio3.append(float(row["price"]))
                
    return(barrios, barrio1, barrio2, barrio3)

