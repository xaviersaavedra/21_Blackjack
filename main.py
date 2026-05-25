import art
import random
def crear_mazo():
    colores = ['♥️', '♦️', '♠️', '♣️']
    cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    nuevo_mazo = []
    for color in colores:
        for carta in cartas:
            nuevo_mazo.append({"carta": carta, "color": color})
    random.shuffle(nuevo_mazo)
    return nuevo_mazo
def repartir_cartas(mano, mazo):
    if mazo:
        mano.append(mazo.pop())
def calcular_suma(mano):
    suma = 0
    for carta in mano:
        suma += carta["carta"]
    return suma
def mostrar_mesa(mano_j, mano_c):
    mostrar_jugador(mano_j)
    mostrar_crupier(mano_c)
def mostrar_jugador(mano_j):
    print(f"Cartas del Jugador: {mano_j}, que suma: {calcular_suma(mano_j)}")
def mostrar_crupier(mano_c):
    print(f"Cartas del crupier: {mano_c}, que suma: {calcular_suma(mano_c)}")
def jugador_pide_carta(mano_jugador, mano_crupier, mazo):
    repartir_cartas(mano_jugador, mazo)
    mostrar_jugador(mano_jugador)
    as_interactivo(mano_jugador)
    mostrar_crupier(mano_crupier)
def primera_mano(mano_jugador, mano_crupier, mazo):
    repartir_cartas(mano_jugador, mazo)
    repartir_cartas(mano_jugador, mazo)
    repartir_cartas(mano_crupier, mazo)
    mostrar_jugador(mano_jugador)
    as_interactivo(mano_jugador)
    mostrar_crupier(mano_crupier)
def crupier(mano_jugador, mano_crupier, mazo):
    crupier_f = True
    while crupier_f:
        repartir_cartas(mano_crupier, mazo)

        # Calculamos las sumas aquí adentro usando la función existente
        suma_crupier = calcular_suma(mano_crupier)
        suma_jugador = calcular_suma(mano_jugador)

        if suma_crupier > 21:
            mostrar_mesa(mano_jugador, mano_crupier)
            print("Jugador ganó")
            crupier_f = False
        elif suma_crupier == suma_jugador:
            mostrar_mesa(mano_jugador, mano_crupier)
            print("Empate")
            crupier_f = False
        elif suma_crupier < 16:
            crupier_f = True
        else:
            if suma_jugador > suma_crupier:
                mostrar_mesa(mano_jugador, mano_crupier)
                print("Jugador ganó")
                crupier_f = False
            else:
                mostrar_mesa(mano_jugador, mano_crupier)
                print("Jugador perdió")
                crupier_f = False
def as_interactivo(mano_jugador):
    for carta in mano_jugador:
        suma_jugador = calcular_suma(mano_jugador)
        if carta["carta"] == 11 and suma_jugador > 21:
            eleccion_as = input("El as puede valer 1 u 11. ¿Qué elegís? 1 o 11: ")
            if eleccion_as == "1":
                carta["carta"] = 1
                mostrar_jugador(mano_jugador)
juego = True
while juego:
    mano_jugador = []
    mano_crupier = []
    mazo = crear_mazo()
    inicio = input("¿Hola Pá, querés jugar al Blackjack? y o n: ")
    if inicio == "y":
        print(art.logo)
        primera_mano(mano_jugador, mano_crupier, mazo)
        if calcular_suma(mano_jugador) == 21:
            print("Blackjack, Jugador ganó")
            continue
        continuar = input("¿Querés una carta más? y o n: ")
        if continuar == "y":
            jugador_pide_carta(mano_jugador, mano_crupier, mazo)
            turno_jugador = True
            while turno_jugador:
                suma_jugador = calcular_suma(mano_jugador)
                if suma_jugador > 21:
                    print("Jugador perdió")
                    turno_jugador = False
                elif suma_jugador == 21:
                    crupier(mano_jugador, mano_crupier, mazo)
                    turno_jugador = False
                else:
                    as_interactivo(mano_jugador)
                    suerte = input("¿Querés otra carta? y o n: ")
                    if suerte == "n":
                        crupier(mano_jugador, mano_crupier, mazo)
                        turno_jugador = False
                    elif suerte == "y":
                        jugador_pide_carta(mano_jugador, mano_crupier, mazo)
        elif continuar == "n":
            crupier(mano_jugador, mano_crupier, mazo)
        else:
            crupier(mano_jugador, mano_crupier, mazo)
    else:
        juego = False