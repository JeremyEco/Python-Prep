
from datetime import date

import os

grados = input("Ingresar los grados centígrados: ")
humedad = input("Ingresar el porcentaje de humedad: ")
lluvia = input("""Indique "si" o "no" si hubo lluvia: """)

if lluvia == "si":
    lluvia = True
elif lluvia == "no":
    lluvia = False

hora = date.today()

archivo = open("Ejercicio_3.txt", "w")
archivo.write("marca_tiempo,grados_centigrados,humedad,lluvia\n")
archivo.write(f"{hora},{grados},{humedad},{lluvia}")
archivo.close()

print("Archivo cargado exitosamente.")