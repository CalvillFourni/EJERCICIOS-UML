class Elipse:
    def __init__(self,color, Eje_mayor, Eje_menor):
        self.color= color
        self.Eje_mayor= Eje_mayor
        self.Eje_menor= Eje_menor
    
    def __str__(self):
        return f" Elipse(color={self.color}, Eje_mayor={self.Eje_mayor}, Eje_menor= {self.Eje_menor})"