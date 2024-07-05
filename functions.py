def imprimir_tauler(tauler, casilla):
    fila = casilla // 3
    columna = casilla % 3
    tauler[fila][columna] = 'O'
    print(tauler[0])
    print(tauler[1])
    print(tauler[2])