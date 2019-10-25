from PUNTO import *
from math import pi

class Figura:

    def __init__(self, p1, p2):
        self.origen = p1
        self.destino = p2
        self.area = 0

class Cuadrado (Figura):

    def calcular_area(self):
        lado = self.origen.calcular_distancia(self.destino)
        self.area = lado * lado

class Circulo(Figura):

    def calcular_area(self):
        radio = self.origen.calcular_distancia(self.destino)
        self.area = pi * (radio ** 2)
