import math


class Circulo:
    def __init__(self, radio, ):
        self.radio = radio
       

    def calcular_area(self):
        a = math.pi * self.radio **2
        print("El area es :" ,a)

    def calcular_perimetro(self):
        p = math.pi * 2 * self.radio
        print("El perimetro es:" ,p)

       


r = int(input("Ingrese el valor del radio: "))
c = Circulo(r)
c.calcular_area()
c.calcular_perimetro()


         


