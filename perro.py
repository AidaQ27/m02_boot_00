class Perro():
    def __init__(self, n, e, p):
        self.nombre = n
        self.edad = e
        self.peso = p
    
    def ladrar(self):
        if self.peso >= 8:
            print('Guau, guau')
        else:
            print('boop, boop')
    
    def __str__(self):
        return"Soy el perro {}".format(self.nombre)
        return"Perro {}, e: {}, p: {}".format(self.nombre, self.edad, self.peso)

