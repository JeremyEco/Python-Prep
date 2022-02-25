
import sys

from datetime import datetime

import os
if len(sys.argv)==4:
    from datetime import date

    import os

    hora = date.today()

    archivo = open("Ejercicio_2.txt", "w")
    archivo.write("marca_tiempo,grados_centigrados,humedad,lluvia\n")
    archivo.write(f"{hora},{sys.argv[1]},{sys.argv[2]},{sys.argv[3]}")
    archivo.close()

    print("Archivo cargado exitosamente.")
else:
    print("Error. No indicó los parámetros completos")