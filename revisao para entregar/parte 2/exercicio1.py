class Quadrado:
    lado = 0

    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado**2


class Triangulo:
    base = 0
    altura = 0

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base*self.altura
