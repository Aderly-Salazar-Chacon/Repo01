import random


def jugar_adivinanza():
    print("¡Bienvenido a Adivina el número!")
    print("Estoy pensando en un número entre 1 y 100. ¿Puedes adivinar cuál es?")

    numero_secreto = random.randint(1, 100)
    intentos = 0

    while True:
        intento = int(input("Introduce tu suposición: "))
        intentos += 1

        if intento < numero_secreto:
            print("El número que estoy pensando es más grande. ¡Inténtalo de nuevo!")
        elif intento > numero_secreto:
            print("El número que estoy pensando es más pequeño. ¡Inténtalo de nuevo!")
        else:
            print(f"¡Felicidades! ¡Has adivinado el número en {intentos} intentos!")
            break


jugar_adivinanza()
