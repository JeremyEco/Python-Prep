import sys

if len(sys.argv) == 4:
    print("El ejercicio es Correcto")
    print("Primer parámetro ", sys.argv[1])
    print("Segundo parámetro ", sys.argv[2])
    print("Tercero parámetro ", sys.argv[3])
else:
    print("Error. Más de 3 parámetros igresados")
    print(sys.argv)