class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
     
    def arearec(self):
        return self.base * self.altura
    
    

base = int(input('Ingresa base : '))
altura = int(input('Ingresa altura :'))
rectangulo1 = Rectangulo(base, altura)

base = int(input('Ingresa base : '))
altura = int(input('Ingresa altura :'))
rectangulo2 = Rectangulo(base, altura)

print(f'El Area del rectangulo1 es : {rectangulo1.arearec()}')
print(f'El Area del rectangulo2 es : {rectangulo2.arearec()}')
    