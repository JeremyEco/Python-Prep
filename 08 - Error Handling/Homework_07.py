
from itertools import count
from random import choice

class funciones:
    def __init__(self, lista):
        if (type(lista) != list):
            self.lista = [0]
            raise ValueError("El dato ingresado no es una lista. Se devuelve [0]")
        else:
            self.lista = lista

    def __confnum(self, numero):
        if (type(numero) == int) or (type(numero) == float):
            return True
        else:
            return False
                
        return conf

    def __primo(self, numero):
        p = True
        if (numero == 0) or (numero == 1):
            p = False
        elif type(numero) != int:
            p = False
        else:
            for i in range(2, numero):
                if numero%i == 0:
                    p = False
                    break
        return p

    def primo(self):
        primos = []
        for i in self.lista:
            if self.__confnum(i):
                primos.append(self.__primo(i))
            else:
                primos.append(False)
        return primos
    
    def rep(self, ind):
        """
        Regresa otra lista con el número que se repita más de una vez en la lista:
        [ número, veces que se repite ]

        Indique ind=1 para arrojar el mayor, ind=0 para arrojar el menor, 
        ind=-1 para arrojar cualquier número. Arroja [0, 0] en cualquier otro caso
        """
        rep = []
        for i in self.lista:
            if self.lista.count(i) >1:
                rep.append(i)
        if len(rep) > 1:
            rep = list(set(rep))
            if ind == 1:
                return [max(rep), self.lista.count(max(rep))]
            elif ind == 0:
                return [min(rep), self.lista.count(min(rep))]
            elif ind == -1:
                azar = choice(rep)
                return [azar, self.lista.count(azar)]
            elif ind == None:
                return [0, 0]
            else:
                return [0, 0]
        else:
            return [0, 0]
    
    def __convgrados(self, grados, origen, destino):
        """
        Retorna la conversión de grados. 
        los datos requeridos son los grados, Celsius (c), Kelvin (k) o Farenheit (f) como 
        datos de origen o de destino.

        Retorna None si no se especifican los grados correctamente.
         Retorna los grados de input si no se especifican correctamente origen o destino.
        """
        valor_destino = None
        if (type(grados) == int) or (type(grados) == float):
            if (origen == destino):
                valor_destino = grados
            elif (origen == 'c') & (destino == 'f'):
                valor_destino = (grados * 9 / 5) + 32
            elif (origen == 'c') & (destino == "k"):
                valor_destino = grados + 273.15
            elif (origen == 'f') & (destino == 'c'):
                valor_destino = (grados - 32) * 5 / 9
            elif (origen == 'f') & (destino == 'k'):
                valor_destino = ((grados - 32) * 5 / 9) + 273.15
            elif (origen == 'k') & (destino == 'c'):
                valor_destino = grados - 273.15
            elif (origen == 'k') & (destino == 'f'):
                valor_destino = ((grados - 273.15) * 9 / 5) + 32
            else:
                valor_destino = grados
        return valor_destino

    def convgrados(self, origen, destino):
        opciones = ["k", "c", "f"]
        if (origen not in opciones) or (destino not in opciones):
            print("No especificó los datos de origen o destino correctamente.")
            return []
        else:
            listaconv = []
            for i in self.lista:
                if self.__confnum(i):
                    listaconv.append(round(self.__convgrados(i, origen, destino),2))
                else:
                    listaconv.append(i)
            return listaconv




            