class Cuadro:
    def __init__(self,titulo,AC,tecnica,subtecnica,soporte,autor,estado_conservacion):
        self.titulo = titulo
        self.AC = AC
        self.tecnica = tecnica
        self.subtecnica = subtecnica
        self.soporte = soporte
        self.autor = autor
        self.estado_conservacion = estado_conservacion

    # ...existing code...
    
    def __str__(self):
        return (
            f"Título: {self.titulo}\n"
            f"AC: {self.AC}\n"
            f"Técnica: {self.tecnica}\n"
            f"Sub-técnica: {self.subtecnica}\n"
            f"Soporte: {self.soporte}\n"
            f"Autor: {self.autor}\n"
            f"Estado de conservación: {self.estado_conservacion}\n"
            f"Se localiza en: {self.lugar if self.lugar else 'No asignado'}"
        )
# ...existing code...

    def se_localiza_en(self,lugar):
        self.lugar=lugar


