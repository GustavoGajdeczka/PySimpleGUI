class circulo:
    def __init__(self, raio):
        self.raio = raio
        self.PI = 3.1415
    
    def area(self):
        return round(((self.raio * self.raio) * self.PI), 2)
