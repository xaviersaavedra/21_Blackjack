import art
import random
colores = ['♥️', '♦️', '♠️', '♣️']
cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
mazo = []
for color in colores:
    for carta in cartas:
        mazo.append({"carta":carta,"color":color})
random.shuffle(mazo)
suma_jugador = 0
suma_crupier = 0
def repartir_cartas(mano):
    mano.append((random.choice(mazo)).copy())
def calcular_suma(mano):
    suma = 0
    for carta in mano:
        suma += carta["carta"]
    return suma
def mostrar_mesa():
    mostrar_jugador()
    mostrar_crupier()
def mostrar_jugador():
    print(f"Cartas del Jugador: {mano_jugador}, que suma:{calcular_suma(mano_jugador)}")
def mostrar_crupier():
    print(f"Cartas del crupier: {mano_crupier}, que suma:{calcular_suma(mano_crupier)}")
def jugador_pide_carta():
    repartir_cartas(mano_jugador)
    actualizar_suma()
    mostrar_jugador()
    as_interactivo()
    actualizar_suma()
    mostrar_crupier()
def primera_mano():
    repartir_cartas(mano_jugador)
    repartir_cartas(mano_jugador)
    repartir_cartas(mano_crupier)
    actualizar_suma()
    mostrar_jugador()
    as_interactivo()
    actualizar_suma()
    mostrar_crupier()
def crupier():
    crupier_f = True
    while crupier_f:
        repartir_cartas(mano_crupier)
        actualizar_suma()
        if suma_crupier > 21:
            mostrar_mesa()
            print("Jugador ganó")
            crupier_f = False
        elif suma_crupier == suma_jugador:
            mostrar_mesa()
            print("Empate")
            crupier_f = False
        elif suma_crupier < 16:
            crupier_f = True
        else:
            if suma_jugador > suma_crupier:
                mostrar_mesa()
                print("Jugador ganó")
                crupier_f = False
            else:
                mostrar_mesa()
                print("Jugador perdió")
                crupier_f = False
def as_interactivo():
    for carta in mano_jugador:
        actualizar_suma()
        if carta["carta"] == 11 and suma_jugador > 21:
            eleccion_as = input("El as puede valer 1 u 11.¿Qué elegís? 1 o 11")
            if eleccion_as == "1":
                carta["carta"] = 1
                actualizar_suma()
                mostrar_jugador()
def actualizar_suma():
    global suma_jugador, suma_crupier
    suma_jugador = calcular_suma(mano_jugador)
    suma_crupier = calcular_suma(mano_crupier)
    return suma_jugador, suma_crupier
juego = True
while juego:
    mano_jugador = []
    mano_crupier = []
    inicio = input("¿Hola Pá,querés jugar al Blackjack? y o n")
    if inicio == "y":
        print(art.logo)
        primera_mano()
        if suma_jugador == 21:
            print("Blackjack,Jugador ganó")
            continue
        continuar = input("¿Querés una carta más? y o n")
        if continuar == "y":
            jugador_pide_carta()
            turno_jugador = True
            while turno_jugador:
                if suma_jugador > 21:
                    print("Jugador perdió")
                    turno_jugador = False
                elif suma_jugador == 21:
                    crupier()
                    turno_jugador = False
                else:
                    as_interactivo()
                    actualizar_suma()
                    suerte = input("¿Querés otra carta? y o n")
                    if suerte == "n":
                        crupier()
                        turno_jugador = False
                    elif suerte == "y":
                        jugador_pide_carta()
        elif continuar == "n":
            crupier()
        else:
            crupier()