# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math

class Treugolnik:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.ab = math.sqrt((b[1] - a[1])**2 + (b[0] - a[0])**2)
        self.bc = math.sqrt((c[1] - b[1])**2 + (c[0] - b[0])**2)
        self.ca = math.sqrt((a[1] - c[1])**2 +(a[0] - c[0])**2)
    def perimetr(self):
        return self.ab + self.bc + self.ca

    def ploshad(self):
        p = self.perimetr() / 2
        s = math.sqrt(p*(p-self.ab)*(p-self.bc)*(p-self.ca))
        return s

    def visota(self):
        h = self.ploshad() / (0.5 * self.ab )
        return h


t = Treugolnik(a=(0,2),b=(2,2), c=(4,0))
print(t.perimetr())
print(t.ploshad())
print(t.visota())