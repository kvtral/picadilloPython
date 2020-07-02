class Auto:
    rojo = False

    def __init__(self, puertas, color):
        
        self.puertas = puertas
        self.color = color

        print ("Se creo un Auto con", puertas, "puertas y de color", color)
        print ("Se creo un Auto con {} puertas y de color {}".format (puertas, color))
    
    def fabricar(self):
        self.rojo = True

    def conf (self):
        if (self.rojo):
            print ("done")
        else:
            print ('vuelva luego')

a = Auto (2,"rojo")

a.fabricar()
a.conf ()

print (a.rojo)


# Mantenemos la misma idea para trabajar con las clases

class Fabrica:
    def __init__(self, tiempo, nombre, ruedas):
        self.tiempo=tiempo
        self.nombre = nombre
        self.ruedas = ruedas
        print ("----ok-----", self.nombre)

    def __del__(self):
        print ("---Deleted---", self.nombre)
    
    def __str__(self):
        return("{} se fabricó con exito. En {} y tiene {}".format (self.nombre, self.tiempo,  self.ruedas))



a = Fabrica (3,"Quinto",4)

print (a.ruedas)