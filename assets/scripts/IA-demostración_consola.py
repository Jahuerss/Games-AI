import math

# Variables
player = True
estat = 0  # 0 = Sin estado, 1 = Gana Jugador, 2 = Gana IA, -1 = Empate
tauler_info = [0, 0, 0, 0, 0, 0, 0, 0, 0]
tauler = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]


# Funciones
def imprimir_tauler(tauler, casilla):
    fila = casilla // 3
    columna = casilla % 3
    tauler[fila][columna] = 'O' if tauler_info[casilla] == 1 else 'X'
    print(tauler[0])
    print(tauler[1])
    print(tauler[2])


def ganador(tauler_info):
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
    ganador(board)
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
        if board[i] == 0:
            board[i] = 2  # La IA juega como '2'
            score = minimax(board, 0, False)
            board[i] = 0
            if score > best_score:
                best_score = score
                move = i
    return move


# Bucle principal del juego
while True:
    ganador(tauler_info)

    if estat == 0:
        if player:  # Turno del jugador
            casilla = int(input("Escoge casilla (1-9): ")) - 1
            if tauler_info[casilla] == 0:
                tauler_info[casilla] = 1  # El jugador humano es '1'
                imprimir_tauler(tauler, casilla)
                player = False
        else:  # Turno de la IA
            ia_move = mejor_movimiento(tauler_info)
            tauler_info[ia_move] = 2  # La IA juega como '2'
            print(f"IA escoge la casilla {ia_move + 1}")
            imprimir_tauler(tauler, ia_move)
            player = True
    elif estat == 1:
        print('Gana Humano')
        break
    elif estat == 2:
        print('Gana IA')
        break
    elif estat == -1:
        print('Empate')
        break