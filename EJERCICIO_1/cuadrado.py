class Cuadrado:
    def __init__(self, longitud, color):
        self.longitud= longitud
        self.color=color

    def __str__(self):
        return f"Cuadrado(Longitud={self.longitud}, color={self.color})"