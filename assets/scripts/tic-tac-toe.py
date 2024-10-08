import fileinput

import pygame, sys, math, time
from pygame.locals import *

# Iniciar Pygame
pygame.init()

# Variables
player = True  # True para jugador humano, False para IA
estat = 0  # 0 = Sin estado, 1 = Gana Jugador, 2 = Gana IA, -1 = Empate
tauler_info = [0, 0, 0, 0, 0, 0, 0, 0, 0]
tauler = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]

# Pantalla
pantalla = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Tic-Tac-Toe')
pantalla.fill((255, 255, 255))

# Cargar imágenes
fons = pygame.image.load('assets/images/tauler.png')
imgX = pygame.image.load('assets/images/X.png')
imgO = pygame.image.load('assets/images/O.png')

# Definir rectángulos
rects = [
    pygame.Rect(0, 0, 182, 173),
    pygame.Rect(202, 0, 213, 173),
    pygame.Rect(436, 0, 182, 173),
    pygame.Rect(0, 193, 182, 173),
    pygame.Rect(202, 193, 213, 173),
    pygame.Rect(436, 193, 182, 173),
    pygame.Rect(0, 426, 182, 173),
    pygame.Rect(202, 426, 213, 173),
    pygame.Rect(436, 426, 182, 173)
]

# Funciones
def imprimir_tauler(casilla):
    fila = casilla // 3
    columna = casilla % 3
    tauler[fila][columna] = 'O' if tauler_info[casilla] == 1 else 'X'
    print(tauler[0])
    print(tauler[1])
    print(tauler[2])

def ganador():
    global estat  # Declarar estat como global
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

    for cond in win_conditions:
        if tauler_info[cond[0]] == tauler_info[cond[1]] == tauler_info[cond[2]] != 0:
            estat = 1 if tauler_info[cond[0]] == 1 else 2
            return

    # Verificar si el tablero está lleno (empate)
    if all([x != 0 for x in tauler_info]):
        estat = -1  # Empate
    else:
        estat = 0  # Juego en progreso

def minimax(board, depth, is_maximizing):
    ganador()
    if estat == 2:
        return 1
    elif estat == 1:
        return -1
    elif estat == -1:
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == 0:
                board[i] = 2
                score = minimax(board, depth + 1, False)
                board[i] = 0
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == 0:
                board[i] = 1
                score = minimax(board, depth + 1, True)
                board[i] = 0
                best_score = min(score, best_score)
        return best_score

# Función para encontrar el mejor movimiento para la IA
def mejor_movimiento(board):
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == 0:  # Solo considera casillas vacías
            board[i] = 2  # La IA juega como '2'
            score = minimax(board, 0, False)
            board[i] = 0
            if score > best_score:
                best_score = score
                move = i
    return move  # Devuelve None si no hay movimientos válidos

# Función para dibujar el tablero y las fichas
def dibujar_tauler():
    pantalla.blit(fons, (0, 0))
    for i in range(9):
        if tauler_info[i] == 1:
            pantalla.blit(imgO, rects[i].topleft)
        elif tauler_info[i] == 2:
            pantalla.blit(imgX, rects[i].topleft)
    pygame.display.update()

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if estat == 0:  # Solo permitir interacciones si el juego no ha terminado
            if event.type == pygame.MOUSEBUTTONDOWN and player:  # Turno del jugador humano
                if event.button == 1:  # Botón izquierdo del ratón
                    for i, rect in enumerate(rects):
                        if rect.collidepoint(event.pos) and tauler_info[i] == 0:
                            tauler_info[i] = 1  # Jugador humano juega como '1'
                            imprimir_tauler(i)
                            player = False
                            break

    # Turno de la IA
    if not player and estat == 0:
        ia_move = mejor_movimiento(tauler_info)
        if ia_move is not None:  # Solo permitir el movimiento si no es None
            tauler_info[ia_move] = 2  # La IA juega como '2'
            print(f"IA escoge la casilla {ia_move + 1}")
            imprimir_tauler(ia_move)
            player = True

    # Comprobar el estado del juego
    ganador()

    # Dibujar el tablero
    dibujar_tauler()

    # Comprobar si hay un ganador o empate
    if estat == 1:
        time.sleep(1)
        break
    elif estat == 2:
        time.sleep(1)
        break
    elif estat == -1:
        time.sleep(1)
        break


pygame.init()
pygame.display.set_caption('Tic-Tac-Toe')
pantalla = pygame.display.set_mode((600, 600))
pantalla.fill((255, 255, 255))
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if estat == -1:
            empate = pygame.image.load('assets/images/empat.png')
            pantalla.blit(empate, (0, 0))
            pygame.display.update()
            time.sleep(3)
            pygame.quit()
            sys.exit()
            break
        elif estat == 1:
            empate = pygame.image.load('assets/images/Jugador-victoria.png')
            pantalla.blit(empate, (0, 0))
            pygame.display.update()
            time.sleep(3)
            pygame.quit()
            sys.exit()
            break
        elif estat == 2:
            empate = pygame.image.load('assets/images/IA-victoria.png')
            pantalla.blit(empate, (0, 0))
            pygame.display.update()
            time.sleep(3)
            pygame.quit()
            sys.exit()
            break






