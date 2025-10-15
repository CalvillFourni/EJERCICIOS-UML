class lugar:
    def __init__(self, ciudad, comunidad, pais):
        self.ciudad=ciudad
        self.comunidad=comunidad
        self.pais=pais

    def __str__(self):
        return(
            f"ciudad: {self.ciudad}\n"
            f"comunidad: {self.comunidad}\n"
            f"pais: {self.pais}\n"
        )