class Cubo:
    def __init__(self,alto,ancho,profundo):
        self.alto = alto
        self.ancho = ancho
        self.profundo = profundo
    
    def calcularvolumen(self):
        return self.alto * self.ancho * self.profundo
    
    

alto = int(input("Ingrese alto del cubo : "))
ancho = int(input("Ingrese ancho del cubo : "))
profundo = int(input("Ingrese profundo del cubo : "))


cubo1obj = Cubo(alto, ancho, profundo)

print(f'El volumen del cubo es : {cubo1obj.calcularvolumen()}')    
        