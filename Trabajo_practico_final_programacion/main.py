import datos
import graficos

#este es el diccionario con todos los datos del csv
csvLista = datos.leer_csv("listings.csv")

datosSimon = datos.precio_prom_por_vecindario(csvLista)
datosJuli = datos.dist_de_precios_segun_el_barrio(csvLista, datosFede)

datosFede = datos.ofertas_por_barrio(csvLista)
datosMarien = datos.diferent_room_types(csvLista)
print(datosMarien)


graficos.plotear_j(datosJuli[0], datosJuli[1], datosJuli[2], datosJuli[3])
graficos.plotear_s(datosSimon.keys(), datosSimon.values())

graficos.plotear_f(datosFede)
graficos.plotear_m(datosMarien)