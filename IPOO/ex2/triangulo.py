class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return round((self.base * self.altura) / 2 ,2)