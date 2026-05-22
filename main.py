from typing import Any

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
suma_maquina = 0
def repartir_cartas(mano):
    mano.append((random.choice(mazo)).copy())
def calcular_suma(mano):
    suma = 0
    for carta in mano:
        suma += carta["carta"]
    return suma
def mostrar_mesa():
    print("Cartas del Jugador:", mano_jugador, "que suma:", suma_jugador)
    print("Cartas de la maquina:", mano_maquina, "que suma:", suma_maquina)

def maquina():
    maquina = True
    while maquina:
        repartir_cartas(mano_maquina)
        actualizar_suma()
        if suma_maquina > 21:
            mostrar_mesa()
            print("Jugador ganó")
            maquina = False
        elif suma_maquina == suma_jugador:
            mostrar_mesa()
            print("Empate")
            maquina = False
        elif suma_maquina < 16:
            maquina = True
        else:
            if suma_jugador > suma_maquina:
                mostrar_mesa()
                print("Jugador ganó")
                maquina = False
            else:
                mostrar_mesa()
                print("Jugador perdió")
                maquina = False
def as_interactivo():
    for carta in mano_jugador:
        actualizar_suma()
        if carta["carta"] == 11 and suma_jugador > 21:
            eleccion_as = input("El as puede valer 1 u 11.¿Qué elegís? 1 o 11")
            if eleccion_as == "1":
                carta["carta"] = 1
                actualizar_suma()
                print("Cartas del Jugador:", mano_jugador, "que suma:", suma_jugador)
def actualizar_suma():
    global suma_jugador, suma_maquina
    suma_jugador = calcular_suma(mano_jugador)
    suma_maquina = calcular_suma(mano_maquina)
    return suma_jugador, suma_maquina
juego = True
while juego:
    mano_jugador = []
    mano_maquina = []
    inicio = input("¿Hola Pá,querés jugar al Blackjack? y o n")
    if inicio == "y":
        print(art.logo)
        repartir_cartas(mano_jugador)
        repartir_cartas(mano_jugador)
        repartir_cartas(mano_maquina)
        actualizar_suma()
        print("Cartas del Jugador:",mano_jugador,"que suma:",suma_jugador)
        as_interactivo()
        actualizar_suma()
        print("Cartas de la maquina:",mano_maquina,"que suma:",suma_maquina)
        if suma_jugador == 21:
            print("Blackjack,Jugador gano")
            continue
        continuar = input("¿Queres una carta mas? y o n")
        if continuar == "y":
            repartir_cartas(mano_jugador)
            actualizar_suma()
            print("Cartas del Jugador:",mano_jugador,"que suma:",suma_jugador)
            as_interactivo()
            actualizar_suma()
            print("Cartas de la maquina:", mano_maquina,"que suma:",suma_maquina)
            suerte_de_pricipiante = True
            while suerte_de_pricipiante:
                if suma_jugador > 21:
                    print("Jugador perdio")
                    suerte_de_pricipiante = False
                elif suma_jugador == 21:
                    maquina()
                    suerte_de_pricipiante = False
                else:
                    as_interactivo()
                    actualizar_suma()
                    suerte = input("¿Queres otra carta? y o n")
                    if suerte == "n":
                        maquina()
                        suerte_de_pricipiante = False
                    elif suerte == "y":
                        repartir_cartas(mano_jugador)
                        actualizar_suma()
                        print("Cartas del Jugador:", mano_jugador, "que suma:", suma_jugador)
                        as_interactivo()
                        actualizar_suma()
                        print("Cartas de la maquina:", mano_maquina, "que suma:", suma_maquina)
        elif continuar == "n":
            maquina()
        else:
            maquina()