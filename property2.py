# Hacer esto no tiene ningun sentido para el calculo que hace.
# Ni tampoco tiene sentido usar el property en este caso 
# Es solo para ilustrar el uso de property 

class Elevador():
    def __init__(self, elevador):
        self.e = elevador

    def calcular(self, num=0):
        # Aca se esta usando el "metodo" que definimos como property, se accede como un atributo
        return num ** self.valor        

    @property
    def valor (self):
        return self.e * 1
    
cuadrado = Elevador(2)
cubo = Elevador(3)

numero = int(input("Ingresa un numero:  "))
print (str (numero) + " elevado al cuadrado es : " + str(cuadrado.calcular(numero)))
print (str (numero) + " elevado al cubo es : " + str (cubo.calcular(numero)))