#!/usr/bin/env python
# coding: utf-8

# ## importamos el modulo de ploteo matplotlib

# In[15]:


from matplotlib import pyplot as plt


# **Función de ploteo de Simon**

# In[16]:


# SIMON
def plotear_s(etiquetas: list, valores : list): 
    titulo = "Precios promedio por vecindarios"
    """
    Genera un gráfico de barras que representa los Precios promedio por vecindarios.
    @author Simón Revello.
    """
    plt.figure(figsize=(15, 6))
    plt.grid(zorder=0)
    plt.bar(etiquetas, valores, color="#10b981", ec="black")
    plt.title(titulo)
    plt.xticks(rotation = 90, fontsize = 8)
    plt.yticks(fontsize=8)
    plt.savefig(titulo + ".png", bbox_inches = 'tight')


# **Función de ploteo de Marien**

# In[17]:


# MARIEN
def plotear_m(diccionario):
    #ajustamos el tamaño de la imagen  
    plt.figure(figsize = (15,6))
    #ploteamos la grafica
    plt.bar(diccionario.keys(), diccionario.values(), color="darkorchid", linewidth=1, edgecolor="black")
    #Ajustamos el tamaño del texto y rotamos mejoramos eje x
    plt.xticks(rotation = 90, fontsize=15);
    plt.yticks(fontsize=20);
    #Añadimos títulos y guardamos la imágen
   
    plt.ylabel('Cantidad de postulaciones',fontsize=15)
    plt.title('Precio promedio según tipo de habitación',fontsize=20)
    plt.savefig('Grafica_Barras_Mallorca.png', bbox_inches = 'tight')


# **Función de ploteo de Federico**

# In[18]:


#FEDERICO
def plotear_f(diccionario):
    #ajustamos el tamaño de la imagen  
    plt.figure(figsize = (15,6))
    #ploteamos la grafica
    plt.bar(diccionario.keys(), diccionario.values(), color="mediumspringgreen", linewidth=1, edgecolor="black")
    #Ajustamos el tamaño del texto y rotamos mejoramos eje x
    plt.xticks(rotation = 90, fontsize=15)
    plt.yticks(fontsize=20)
    #Añadimos títulos y guardamos la imágen
    plt.xlabel('Vecindarios',fontsize=15)
    plt.ylabel('Cantidad de postulaciones',fontsize=15)
    plt.title('Cantidad de ofertas por sectores en Mallorca de un Total de 17795 posteos',fontsize=20);
    plt.savefig('Ofertas_por_barrio.png', bbox_inches = 'tight')


# **Función de ploteo de Julian**

# In[19]:


# JULI
def plotear_j(barrios, barrio1, barrio2, barrio3):
    #ajustamos el tamaño de la imagen  
    plt.figure(figsize=(15,6))
    #ploteamos la grafica
    plt.hist(barrio1, bins=100, range=[0, 400], color="#9d5353", ec="black")
    #Ajustamos el tamaño del texto y rotamos mejoramos eje x
    plt.xticks(rotation=90,fontsize=15);
    plt.yticks(fontsize=20);
    #Añadimos títulos y guardamos la imágen
    plt.xlabel('Precio',fontsize=15)
    plt.ylabel('Frecuencia',fontsize=15)
    plt.title('Distribucion de precios en el barrio {}'.format(barrios[0]["nombre"]),fontsize=20);
    plt.savefig('Distr_De_Precios_Segun_El_Barrio_{}.png'.format(barrios[0]["nombre"]), bbox_inches = 'tight')

    #ajustamos el tamaño de la imagen  
    plt.figure(figsize=(15,6))
    #ploteamos la grafica
    plt.hist(barrio2, bins=100, range=[0, 400], color="#9d5353", ec="black")
    #Ajustamos el tamaño del texto y rotamos mejoramos eje x
    plt.xticks(rotation=90,fontsize=15);
    plt.yticks(fontsize=20);
    #Añadimos títulos y guardamos la imágen
    plt.xlabel('Precio',fontsize=15)
    plt.ylabel('Frecuencia',fontsize=15)
    plt.title('Distribucion de precios en el barrio {}'.format(barrios[1]["nombre"]),fontsize=20);
    plt.savefig('Distr_De_Precios_Segun_El_Barrio_{}.png'.format(barrios[1]["nombre"]), bbox_inches = 'tight')

    #ajustamos el tamaño de la imagen  
    plt.figure(figsize=(15,6))
    #ploteamos la grafica
    plt.hist(barrio3, bins=100, range=[0, 400], color="#9d5353", ec="black")
    #Ajustamos el tamaño del texto y rotamos mejoramos eje x
    plt.xticks(rotation=90,fontsize=15);
    plt.yticks(fontsize=20);
    #Añadimos títulos y guardamos la imágen
    plt.xlabel('Precio',fontsize=15)
    plt.ylabel('Frecuencia',fontsize=15)
    plt.title('Distribucion de precios en el barrio {}'.format(barrios[2]["nombre"]),fontsize=20);
    plt.savefig('Distr_De_Precios_Segun_El_Barrio_{}.png'.format(barrios[2]["nombre"]), bbox_inches = 'tight')

