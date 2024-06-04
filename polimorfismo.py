from math import sqrt


class EquiFigura:
    def __init__(self, longitudLados):
        self.__longitudLados = longitudLados

    def getLongitudLados(self):
        return self.__longitudLados

    def setgetLongitudLados(self, longitudLados):
        self.__longitudLados = longitudLados


class TrianguloEquilatero(EquiFigura):
    def getPerimetro(self):
        return self.getLongitudLados() * 3

    def getArea(self):
        return (sqrt(3)*pow(self.getLongitudLados(),2))/4


class Cuadrado(EquiFigura):
    def getPerimetro(self):
        return self.getLongitudLados() * 4

    def getArea(self):
        return pow(self.getLongitudLados(), 2)

te1 = TrianguloEquilatero(3)

cu1 = Cuadrado(4)

print(te1.getArea())
print(te1.getPerimetro())

print(cu1.getArea())
print(cu1.getPerimetro())
