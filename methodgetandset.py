class People:
     def __init__(self, nombre, apellido, edad):
        self._nombre = nombre #se agrega _ para indicar que se esta encapsulando un valor
        self.apellido = apellido
        self.edad = edad
    
     @property # es un decorador que modifica el comportamiento de un método
     def nombre(self): #en este caso recupera el valor de nombre 
         return self._nombre    
        
     @nombre.setter
     def nombre(self, nombre):
         self._nombre = nombre   
         
     def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self.apellido} {self.edad}')
        
 
#nota si vemos a un atributo con un _ indica como buena practica no acceder a el : ejemplo _nombre
        
        
# si quitamos el método set indica que es una variable de solo lectura.      

persona1 = People('Juan', 'Perez', 30)
print(persona1.nombre) # se llama de manera indirecta al método y recupera el valor de nombre.
persona1.nombre = 'Argui Lara'
print(persona1.nombre)         