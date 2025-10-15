class edificio:
    def __init__(self, nombre, culto, inicio_construccion ,fin_construccion ,consagrada , ultima_etapa_construccion ,consagracion_definitiva , BIC ,material, estilo):
        self.nombre=nombre
        self.culto=culto
        self.inicio_construccion=inicio_construccion
        self.fin_construccion=fin_construccion
        self.consagrada=consagrada
        self.ultima_etapa_construccion=ultima_etapa_construccion
        self.consagracion_definitiva=consagracion_definitiva
        self.BIC=BIC
        self.material=material
        self.estilo=estilo

    def se_encuentra_en(self,lugar):
        self.lugar=lugar
        
    
    def __str__(self):
        return(
            f"nombre:{self.nombre}\n"
            f"culto: {self.culto}\n"
            f"inicio construcción:{self.inicio_construccion}\n"
            f"fin construcción:{self.fin_construccion}\n"
            f"consagración:{self.consagrada}"
            f"última etapa construcción: {self.ultima_etapa_construccion}\n"
            f"consagración definitiva: {self.consagracion_definitiva}\n"
            f"BIC: {self.BIC}\n"
            f"material: {self.material}\n"
            f"estilo: {self.estilo}\n"
        )
