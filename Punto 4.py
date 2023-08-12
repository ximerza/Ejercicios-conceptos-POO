class Rectangulo:
    def __init__(self, basex, alturax):
        self.base = basex
        self.altura = alturax
    
    def Area(self):
        a = self.base * self.altura
        print("El area es :", a)

    def Perimetro(self):
        p = 2 * (self.base + self.altura)
        print("El perimetro es :", p)

    def Rectangulo_cuadrado(self):
        if self.base == self.altura:
            print("Es un cuadrado ")

        else:
            print("Es un rectangulo")

b = float(input("Ingrese la base :"))
a = float(input("Ingrese la altura :"))   

r = Rectangulo(b,a)
r.Area()
r.Perimetro()
r.Rectangulo_cuadrado()



        