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
def repartir_cartas(mano):
    mano.append(mazo.pop())
def calcular_suma(mano):
    suma = 0
    for carta in mano:
        suma += carta["carta"]
    return suma


def maquina():
    maquina = True
    while maquina:
        repartir_cartas(mano_maquina)
        suma_maquina = calcular_suma(mano_maquina)
        if suma_maquina > 21:
            print("Cartas del Jugador:", mano_jugador, "que suma:", suma_jugador)
            print("Cartas de la maquina:", mano_maquina, "que suma:", suma_maquina)
            print("Jugador gano")
            maquina = False
        elif suma_maquina == suma_jugador:
            print("Cartas del Jugador:", mano_jugador, "que suma:", suma_jugador)
            print("Cartas de la maquina:", mano_maquina, "que suma:", suma_maquina)
            print("Empate")
            maquina = False
        elif suma_maquina < 16:
            maquina = True
        else:
            if suma_jugador > suma_maquina:
                print("Cartas del Jugador:", mano_jugador, "que suma:", suma_jugador)
                print("Cartas de la maquina:", mano_maquina, "que suma:", suma_maquina)
                print("Jugador gano")
                maquina = False
            else:
                print("Cartas del Jugador:", mano_jugador, "que suma:", suma_jugador)
                print("Cartas de la maquina:", mano_maquina, "que suma:", suma_maquina)
                print("Jugador perdio")
                maquina = False
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
        suma_jugador = calcular_suma(mano_jugador)
        suma_maquina = calcular_suma(mano_maquina)
        print("Cartas del Jugador:",mano_jugador,"que suma:",suma_jugador)
        print("Cartas de la maquina:",mano_maquina,"que suma:",suma_maquina)
        continuar = input("¿Queres una carta mas? y o n")
        if continuar == "y":
            repartir_cartas(mano_jugador)
            suma_jugador = calcular_suma(mano_jugador)
            print("Cartas del Jugador:",mano_jugador,"que suma:",suma_jugador)
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
                    suerte = input("¿Queres otra carta? y o n")
                    if suerte == "n":
                        maquina()
                        suerte_de_pricipiante = False
                    elif suerte == "y":
                        repartir_cartas(mano_jugador)
                        suma_jugador = calcular_suma(mano_jugador)
                        print("Cartas del Jugador:", mano_jugador, "que suma:", suma_jugador)
                        print("Cartas de la maquina:", mano_maquina, "que suma:", suma_maquina)
        elif continuar == "n":
            maquina()
        else:
            maquina()









# def jugada():
#     jugador1 = [mazo.pop() for _ in range(2)]
#     jugador = 0
#     for carta in jugador1:
#         jugador += carta["carta"]
#     # mano_jugador.append({"jugador1":jugador1})
#     return jugador1,jugador
# if inicio == "y":
#     primera_jugada = [mazo.pop() for _ in range(2)]
#     mano_jugador[0] = primera_jugada
#     primera_maquina = [mazo.pop() for _ in range(1)]
#     mano_maquina[0] = primera_maquina
#     print(f"Cartas del Jugador:",[mano_jugador][0],"que suma:")
#     print(f"Cartas de la Máquina:", [mano_maquina][0],"suma:")
# #
# juego = True
# while juego:
#     if inicio == "y":
#         jugada_1()
#         datos = resultado
#         pregunta_continuar = True
#         while pregunta_continuar:
#             continuar = input("¿Queres mas cartas? y o n")
#             if continuar =="y":
#                 mano_jugador2 = ([mazo.pop() for _ in range(1)]+resultado["mano_jugador"])
#                 suma_jugador2 = 0
#                 for carta in mano_jugador2:
#                     suma_jugador2 += carta["carta"]
#                 print(f"Cartas del Jugador:", mano_jugador2,"suma:",{suma_jugador2})












#
# # print("Cartas restantes no baralho:", len(mazo))

# def distribuir_cartas(mazo, num_jogadores, cartas_por_jogador):
#     maos = []
#     for i in range(num_jogadores):
#         # Remove cartas do topo do baralho (final da lista)
#         mao = [mazo.pop() for _ in range(cartas_por_jogador)]
#         maos.append(mao)
#     return maos


# jugador = random.choice(cards)
# jugador2 = random.choice(cards)
# crupier = random.choice(cards)
# while juego:
#     if inicio == "y":
#         print((jugador),(jugador2))
#         print(crupier)
#         juego = False

# 1. Criar o baralho

# valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
# baralho = [f'{v}{n}' for n in naipes for v in valores]
#
# # 2. Embaralhar as cartas
# random.shuffle(baralho)
#
# # 3. Função para distribuir
# def distribuir_cartas(baralho, num_jogadores, cartas_por_jogador):
#     maos = []
#     for i in range(num_jogadores):
#         # Remove cartas do topo do baralho (final da lista)
#         mao = [baralho.pop() for _ in range(cartas_por_jogador)]
#         maos.append(mao)
#     return maos
#
# # Exemplo: 2 jogadores com 5 cartas cada
# jogadores = distribuir_cartas(baralho, 2, 5)
#
# # 4. Mostrar o resultado
# for i, mao in enumerate(jogadores):
#     print(f'Jogador {i+1}: {mao}')
#
# print(f'Cartas restantes: {len(baralho)}')