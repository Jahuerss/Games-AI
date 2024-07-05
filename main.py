from functions import imprimir_tauler

tauler_info = [0, 0, 0, 0, 0, 0, 0, 0, 0]
tauler = [
    ['','',''],
    ['','',''],
    ['','','']
]
player = True

while True:
    if player == True:
        casilla = int(input("Escoge casilla (1-9): ")) - 1
        tauler_info[casilla] = 1
        imprimir_tauler(tauler, casilla)
        player = False
    else:
        print('Test')
        player = True




