class Persona:
    def __init__(self, nombre, apellido, sexo, apellido_nacimiento=None):
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
        self.apellido_nacimiento = apellido_nacimiento
        self.conyuge = None
        self.padres = []

    def casar_con(self, otra_persona):
        self.conyuge = otra_persona
        otra_persona.conyuge = self

    def agregar_padre(self, padre):
        self.padres.append(padre)

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        if self.apellido_nacimiento:
            print(f"Apellido de nacimiento: {self.apellido_nacimiento}")
        print(f"Sexo: {self.sexo}")
        if self.conyuge:
            print(f"Casado con: {self.conyuge.nombre}")
        if self.padres:
            print("Padres: " + ", ".join([padre.nombre for padre in self.padres]))
        print("-" * 30)

# Instancias según el diagrama
kate = Persona("Kate", "Windsor", "Mujer", "Middleton")
guillermo = Persona("Guillermo", "Windsor", "Hombre")
diana = Persona("Diana", "Windsor", "Mujer", "Spencer")
carlos = Persona("Carlos", "Windsor", "Hombre")

# Relaciones de matrimonio
kate.casar_con(guillermo)
diana.casar_con(carlos)

# Relaciones de padres
guillermo.agregar_padre(carlos)
guillermo.agregar_padre(diana)