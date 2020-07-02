class Persona:
    def __init__(self,nombre="Desconocido", edad=0):
        self.nombre = nombre
        self.edad = edad
        
    def beber(self):
        if self.edad < 18:
            print (self.nombre + " es menor de edad")
            return None
        print (self.nombre + " tiene " + str(self.edad) + " por lo que puede beber")
        
    @classmethod
    def metodoClase(cls, argumento=None):
        print ("Soy un metodo de clase, el argumento que me diste fue: " + argumento)

    
    @staticmethod
    def metodoEstatico():
        print ("Soy un metodo estatico, no requiero argumentos cls ni self")
        print ("Quizas prefiero ser una Función, pero bah, depende de ti y de la abstracción")
        
alvaro = Persona("Alvaro", 19)

jorge = Persona("Javier", 15)

alvaro.beber()

jorge.beber()

Persona.metodoClase("Alvaro")

alvaro.metodoEstatico()
