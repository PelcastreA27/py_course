class Aritmetica:
    """
    With  this class you can to make sum, rest, etc.
    """
    def __init__(self, opa, opb):
        self.opa = opa
        self.opb = opb
        
    def sumar(self):
        return self.opa + self.opb  
    
    def restar(self):
        return self.opa - self.opb
    
    def multiplicar(self):
        return self.opa * self.opb
    
    def dividir(self):
        return self.opa / self.opb
    
operacion1 = Aritmetica(1200,5800)
operacion2 = Aritmetica(1200,5800)
operacion3 = Aritmetica(14,14)
operacion4 = Aritmetica(500,60)

print(f'Resultado Suma: {operacion1.sumar()}')
print(f'Resultado Resta : {operacion2.restar()}')
print(f'Resultado Multiplicación : {operacion3.multiplicar()}')      
print(f'Resultado división : {operacion4.dividir():.2f}')        