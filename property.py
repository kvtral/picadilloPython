class Circulo:
    
    def __init__(self, radio):
        self.radio = radio

    
    @property
    def area (self):
        return 3.1416 * (self.radio**2)
    


c = Circulo(5)

print (c.area)