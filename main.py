#Variables
player = True
estat = 0 #Estableix l'estat en el que esta el joc (0 = Sense estat, 1 = Guanyador Jugador, 2 = Guanyador IA, -1 = Empat)
tauler_info = [0, 0, 0, 0, 0, 0, 0, 0, 0]
tauler = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]

#Funcions
def imprimir_tauler(tauler, casilla):
    fila = casilla // 3
    columna = casilla % 3
    tauler[fila][columna] = 'O'
    print(tauler[0])
    print(tauler[1])
    print(tauler[2])

def ganador(tauler_info):
    global estat  # Declarar estat como global
    if tauler_info[0] == 1 and tauler_info[1] == 1 and tauler_info[2] == 1:
        estat = 1
    elif tauler_info[0] == 1 and tauler_info[3] == 1 and tauler_info[6] == 1:
        estat = 1
    elif tauler_info[6] == 1 and tauler_info[7] == 1 and tauler_info[8] == 1:
        estat = 1
    elif tauler_info[2] == 1 and tauler_info[5] == 1 and tauler_info[8] == 1:
        estat = 1
    elif tauler_info[1] == 1 and tauler_info[4] == 1 and tauler_info[7] == 1:
        estat = 1
    elif tauler_info[3] == 1 and tauler_info[4] == 1 and tauler_info[5] == 1:
        estat = 1
    elif tauler_info[0] == 1 and tauler_info[4] == 1 and tauler_info[8] == 1:
        estat = 1
    elif tauler_info[2] == 1 and tauler_info[4] == 1 and tauler_info[6] == 1:
        estat = 1
    elif tauler_info[0] == 2 and tauler_info[1] == 2 and tauler_info[2] == 2:
        estat = 2
    elif tauler_info[0] == 2 and tauler_info[3] == 2 and tauler_info[6] == 2:
        estat = 2
    elif tauler_info[6] == 2 and tauler_info[7] == 2 and tauler_info[8] == 2:
        estat = 2
    elif tauler_info[2] == 2 and tauler_info[5] == 2 and tauler_info[8] == 2:
        estat = 2
    elif tauler_info[1] == 2 and tauler_info[4] == 2 and tauler_info[7] == 2:
        estat = 2
    elif tauler_info[3] == 2 and tauler_info[4] == 2 and tauler_info[5] == 2:
        estat = 2
    elif tauler_info[0] == 2 and tauler_info[4] == 2 and tauler_info[8] == 2:
        estat = 2
    elif tauler_info[2] == 2 and tauler_info[4] == 2 and tauler_info[6] == 2:
        estat = 2

# Bucle principal del juego
while True:
    if player == True:
        ganador(tauler_info)
        if estat == 0:
            casilla = int(input("Escoge casilla (1-9): ")) - 1
            tauler_info[casilla] = 1
            print(tauler_info)
            imprimir_tauler(tauler, casilla)
            player = False
        elif estat == 1:
            print('Gana Humano')
            break
        elif estat == 2:
            print('Gana IA')
            break
    else:
        player = True
