
from random import choice

class vehicle:
    def __init__(self, tipo, color, cilindrada):
        self.tipo = tipo
        self.color = color
        self.cil = cilindrada
        self.velocidad = 0
        self.giro = 0
    
    def acelerar(self, aceleracion):
        self.velocidad += aceleracion
    
    def frenar(self, freno):
        self.velocidad -= freno
        if self.velocidad < 0:
            self.velocidad = 0

    def doblar(self, grados):
        self.giro += grados
    
    def info(self):
        print(f"Vehículo tipo: {self.tipo}, Color: {self.color}, Cilindrada: {self.cil}")

    def estado(self):
        print(f"""El vehículo {self.tipo}: 
        tiene una velocidad de {self.velocidad}
        y un giro de {self.giro}""")

#########################################
#1)

v1 = vehicle("Auto", "Rojo", "600 cc")

##########################################
#2)

v1.acelerar(60)
print(v1.velocidad)
v1.frenar(40)
print(v1.velocidad)
v1.doblar(45)
print(v1.giro)

##########################################
#3)

v2 = vehicle("Camion", "Blanco", "900 cc")
v2.acelerar(50)
print(f"El vehículo {v2.tipo} tiene una velocidad de {v2.velocidad}")

v3 = vehicle("Moto", "Negro", "400 cc")
v3.doblar(145)
print(f"El vehículo {v3.tipo} tiene una giro de {v3.giro} grados")

#########################################
#4)

v1.estado()
v1.info()

#########################################
#5)

class funciones:
    def __init__(self):
        pass

    def __entero(self, numero):
        v = True
        if type(numero) != int:
            v = False
        else:
            if numero < 0:
                v = False
        return v
    
    def primo(self, numero):
        p = True
        if self.__entero(numero):
            if (numero == 0) or (numero == 1):
                p = False
            else:
                for i in range(2, numero):
                    if numero%i == 0:
                        p = False
                        break
        else:
            p = False
        return p
    
    def rep(self, lista, ind):
        """
        Regresa otra lista con el número que se repita más de una vez en la lista:
        [ número, veces que se repite ]

        Indique ind=1 para arrojar el mayor, ind=0 para arrojar el menor, 
        ind=-1 para arrojar cualquier número
        """
        rep = []
        for i in lista:
            if lista.count(i) >1:
                rep.append(i)
        rep = list(set(rep))
        if ind == 1:
            return [max(rep), lista.count(max(rep))]
        elif ind == 0:
            return [min(rep), lista.count(min(rep))]
        elif ind == -1:
            azar = choice(rep)
            return [azar, lista.count(azar)]
        else:
            return None


f = funciones()
print(f.primo(5))
print(f.primo(9))

lista1 = [1,2,3,3,2,2,5,7,7]
print(f.rep(lista1, -1))

            