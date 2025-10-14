
##ejercicio 1

from EJERCICIO_1.circulo import Circulo
from EJERCICIO_1.cuadrado import Cuadrado
from EJERCICIO_1.elipse import Elipse
from EJERCICIO_1.rectángulo import Rectagulo
if __name__ == "__main__":
    c1 = Circulo("Negro", 1)
    c2 = Cuadrado(1.5,"Azul")
    c3 = Elipse("amarillo",3,1)
    c4 = Rectagulo (3,1,"Naranja")
    print(c1)
    print(c2)
    print(c3)
    print(c4)

##ejercicio 2

from EJERCICIO_2.persona import kate, guillermo, diana, carlos

def main():
    kate.mostrar_info()
    guillermo.mostrar_info()
    diana.mostrar_info()
    carlos.mostrar_info()

if __name__ == "__main__":
    main()


##ejercicio 3
from EJERCICO_3.Cuadro import Cuadro
from EJERCICO_3.Lugar import Lugar
if __name__ == "__main__":
    # Crear lugares
    louvre = Lugar("Museo del Louvre", "Paris", "Francia")
    prado = Lugar("Museo de El Prado", "Madrid", "España")

    # Crear cuadros
    original = Cuadro(
        titulo="La Gioconda",
        AC="1503 - 1516",
        tecnica="Óleo",
        subtecnica="Sfumato",
        soporte="Madera de álamo",
        autor="Leonardo da Vinci",
        estado_conservacion="Regular"
    )

    replica = Cuadro(
        titulo="Gioconda de El Prado",
        AC="1503 - 1516",
        tecnica="Óleo",
        subtecnica="Pincelada simple",
        soporte="Madera de nogal",
        autor="Desconocido",
        estado_conservacion="Bueno"
    )

    # Relacionar cuadros con lugares
    original.se_localiza_en(louvre)
    replica.se_localiza_en(prado)

    # Imprimir información
    print(original)
    print()
    print(replica)