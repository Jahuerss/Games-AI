import pygame, sys, math, time
from pygame.locals import *

# Inicialitzar Pygame
pygame.init()

# Variables
jugador = True  # True per al jugador humà, False per a la IA
estat = 0  # 0 = Sense estat, 1 = Guanya el jugador, 2 = Guanya la IA, -1 = Empat
tauler_info = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # Estat de cada casella del tauler
tauler = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]

# Pantalla
pantalla = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Tic-Tac-Toe')  # Títol de la finestra
pantalla.fill((255, 255, 255))  # Fons blanc de la pantalla

# Carregar imatges
fons = pygame.image.load('assets/images/tauler.png')  # Fons del tauler
imatgeX = pygame.image.load('assets/images/X.png')  # Imatge per a 'X'
imatgeO = pygame.image.load('assets/images/O.png')  # Imatge per a 'O'
icona = pygame.image.load('assets/images/icono.png')  # Imatge per la icona

#Mostrar la icona
pygame.display.set_icon(icona)

# Definir rectangles per a les caselles del tauler
rectangles = [
    pygame.Rect(0, 0, 184, 184),
    pygame.Rect(210, 0, 184, 184),
    pygame.Rect(420, 0, 184, 184),
    pygame.Rect(0, 210, 184, 184),
    pygame.Rect(210, 210, 184, 184),
    pygame.Rect(420, 210, 184, 184),
    pygame.Rect(0, 420, 184, 184),
    pygame.Rect(210, 420, 184, 184),
    pygame.Rect(420, 420, 184, 184),
]

# Colors de fons per a cada casella
colors_fons = [
    (85, 107, 47),  # Verd fosc
    (144, 238, 144),  # Verd clar
    (85, 107, 47),  # Verd fosc
    (144, 238, 144),  # Verd clar
    (85, 107, 47),  # Verd fosc
    (144, 238, 144),  # Verd clar
    (85, 107, 47),  # Verd fosc
    (144, 238, 144),  # Verd clar
    (85, 107, 47)   # Verd fosc
]

# Funció per imprimir l'estat del tauler al terminal
def imprimir_tauler(casella):
    fila = casella // 3
    columna = casella % 3
    tauler[fila][columna] = 'O' if tauler_info[casella] == 1 else 'X'  # Assigna 'O' o 'X'
    print(tauler[0])
    print(tauler[1])
    print(tauler[2])

# Funció per comprovar si hi ha un guanyador
def guanyador():
    global estat  # Es declara 'estat' com a variable global per modificar-lo dins de la funció
    condicions_guany = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

    for cond in condicions_guany:
        if tauler_info[cond[0]] == tauler_info[cond[1]] == tauler_info[cond[2]] != 0:  # Comprova si hi ha una fila, columna o diagonal guanyadora
            estat = 1 if tauler_info[cond[0]] == 1 else 2  # Si guanya el jugador (1) o la IA (2)
            return

    # Comprovar si el tauler està ple (empate)
    if all([x != 0 for x in tauler_info]):
        estat = -1  # Empat
    else:
        estat = 0  # El joc continua

# Funció minimax per calcular el millor moviment de la IA
def minimax(tauler, profunditat, es_maximitzant):
    guanyador()  # Comprovar si hi ha un guanyador després de cada moviment
    if estat == 2:  # Si la IA guanya
        return 1
    elif estat == 1:  # Si el jugador guanya
        return -1
    elif estat == -1:  # Si hi ha un empat
        return 0

    if es_maximitzant:
        millor_puntuacio = -math.inf
        for i in range(9):
            if tauler[i] == 0:  # Si la casella està buida
                tauler[i] = 2  # La IA fa el moviment (jugant com '2')
                puntuacio = minimax(tauler, profunditat + 1, False)  # Calcula la puntuació per a la IA
                tauler[i] = 0  # Revertir el moviment
                millor_puntuacio = max(puntuacio, millor_puntuacio)  # Tria el millor moviment
        return millor_puntuacio
    else:
        millor_puntuacio = math.inf
        for i in range(9):
            if tauler[i] == 0:  # Si la casella està buida
                tauler[i] = 1  # El jugador fa el moviment (jugant com '1')
                puntuacio = minimax(tauler, profunditat + 1, True)  # Calcula la puntuació per al jugador
                tauler[i] = 0  # Revertir el moviment
                millor_puntuacio = min(puntuacio, millor_puntuacio)  # Tria el millor moviment per al jugador
        return millor_puntuacio

# Funció per trobar el millor moviment per a la IA
def millor_moviment(tauler):
    millor_puntuacio = -math.inf
    moviment = None
    for i in range(9):
        if tauler[i] == 0:  # Només considera caselles buides
            tauler[i] = 2  # La IA juga com '2'
            puntuacio = minimax(tauler, 0, False)
            tauler[i] = 0  # Revertir el moviment
            if puntuacio > millor_puntuacio:
                millor_puntuacio = puntuacio
                moviment = i  # Guardar el millor moviment
    return moviment  # Retorna el millor moviment (o None si no hi ha cap moviment vàlid)

# Funció per dibuixar el tauler i les fitxes
def dibuixar_tauler():
    pantalla.blit(fons, (0, 0))  # Dibuixa el fons del tauler
    for i, rect in enumerate(rectangles):
        pygame.draw.rect(pantalla, colors_fons[i], rect)  # Dibuixa el fons de cada casella amb un color
        if tauler_info[i] == 1:
            pantalla.blit(imatgeO, rect.topleft)  # Dibuixa la fitxa 'O' per al jugador
        elif tauler_info[i] == 2:
            pantalla.blit(imatgeX, rect.topleft)  # Dibuixa la fitxa 'X' per a la IA

    pygame.display.update()  # Actualitzar la pantalla

# Definir rectangles per als botons de reinici i sortir
boton_reinicio = pygame.Rect(125, 500, 150, 40)  # Botó de reinici del joc
boton_sortir = pygame.Rect(325, 500, 150, 40)  # Botó per sortir del joc

# Funció per reiniciar el joc
def reiniciar_joc():
    global estat, jugador, tauler_info, tauler
    estat = 0  # Restablir l'estat del joc
    jugador = True  # Torn del jugador humà
    tauler_info = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # Reiniciar l'estat de les caselles
    tauler = [
        ['', '', ''],
        ['', '', ''],
        ['', '', '']
    ]
    pantalla.fill((255, 255, 255))  # Netejar la pantalla
    dibuixar_tauler()  # Dibuixar el tauler buit

# Funció per dibuixar el botó de reinici
def dibuixar_boto_reinicio():
    pygame.draw.rect(pantalla, (0, 128, 0), boton_reinicio)  # Dibuixar el botó de reinici en verd
    font = pygame.font.Font(None, 36)
    text = font.render("Reiniciar", True, (255, 255, 255))  # Text del botó en blanc
    pantalla.blit(text, (boton_reinicio.x + (boton_reinicio.width - text.get_width()) // 2, boton_reinicio.y + 5))  # Dibuixar el text
    pygame.display.update()

# Funció per dibuixar el botó de sortir
def dibuixar_boto_sortir():
    pygame.draw.rect(pantalla, (255, 0, 0), boton_sortir)  # Dibuixar el botó de sortir en vermell
    font = pygame.font.Font(None, 36)
    text = font.render("Sortir", True, (255, 255, 255))  # Text del botó en blanc
    pantalla.blit(text, (boton_sortir.x + (boton_sortir.width - text.get_width()) // 2, boton_sortir.y + 5))  # Dibuixar el text
    pygame.display.update()

# Bucle principal del joc
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if estat == 0:  # Permetre només interaccions si el joc no ha acabat
            if event.type == pygame.MOUSEBUTTONDOWN and jugador:  # Torn del jugador humà
                if event.button == 1:  # Botó esquerre del ratolí
                    for i, rect in enumerate(rectangles):
                        if rect.collidepoint(event.pos) and tauler_info[i] == 0:  # Si la casella està buida
                            tauler_info[i] = 1  # El jugador fa el moviment (jugant com '1')
                            imprimir_tauler(i)
                            jugador = False  # Torn per a la IA
                            break

    if not jugador and estat == 0:  # Torn de la IA
        moviment_ia = millor_moviment(tauler_info)  # Obtenir el millor moviment per a la IA
        if moviment_ia is not None:  # Si hi ha un moviment vàlid
            tauler_info[moviment_ia] = 2  # La IA fa el moviment (jugant com '2')
            print(f"IA escull la casella {moviment_ia + 1}")
            imprimir_tauler(moviment_ia)
            jugador = True  # Torn per al jugador humà

    guanyador()  # Comprovar si hi ha un guanyador

    dibuixar_tauler()  # Dibuixar el tauler actualitzat

    # Comprovar si hi ha un guanyador o un empat
    if estat in [1, 2, -1]:
        time.sleep(1)
        if estat == 1:
            victoria = pygame.image.load('assets/images/Jugador-victoria.png')
            pantalla.blit(victoria, (0, 0))  # Mostrar imatge de victòria per al jugador
        elif estat == 2:
            victoria = pygame.image.load('assets/images/IA-victoria.jpg')
            pantalla.blit(victoria, (0, 0))  # Mostrar imatge de victòria per a la IA
        elif estat == -1:
            empat = pygame.image.load('assets/images/empat.jpg')
            pantalla.blit(empat, (0, 0))  # Mostrar imatge de empat

        pygame.display.update()  # Actualitzar la pantalla
        dibuixar_boto_reinicio()  # Mostrar el botó de reinici
        dibuixar_boto_sortir()  # Mostrar el botó de sortir

        botons_procesats = False  # Flag per assegurar-se que els botons es processen només una vegada
        while not botons_procesats:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and boton_reinicio.collidepoint(event.pos):  # Si es fa clic en el botó de reinici
                        reiniciar_joc()
                        botons_procesats = True
                    elif event.button == 1 and boton_sortir.collidepoint(event.pos):  # Si es fa clic en el botó de sortir
                        pygame.quit()
                        sys.exit()
