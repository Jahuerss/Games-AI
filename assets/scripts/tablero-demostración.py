import pygame, sys
from pygame.locals import *

pygame.init()

tauler_info = [0, 0, 0, 0, 0, 0, 0, 0, 0]

pantalla = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Tic-Tac-Toe')
pantalla.fill((255, 255, 255))

rect1 = pygame.Rect(0, 0, 182, 173)
imgrect1X = pygame.image.load('assets/X.png')
imgrect1O = pygame.image.load('assets/O.png')

rect2 = pygame.Rect(202, 0, 213, 173)
imgrect2X = pygame.image.load('assets/X.png')
imgrect2O = pygame.image.load('assets/O.png')

rect3 = pygame.Rect(436, 0, 182, 173)
imgrect3X = pygame.image.load('assets/X.png')
imgrect3O = pygame.image.load('assets/O.png')

rect4 = pygame.Rect(0, 193, 182, 173)
imgrect4X = pygame.image.load('assets/X.png')
imgrect4O = pygame.image.load('assets/O.png')

rect5 = pygame.Rect(202, 193, 213, 173)
imgrect5X = pygame.image.load('assets/X.png')
imgrect5O = pygame.image.load('assets/O.png')

rect6 = pygame.Rect(436, 193, 182, 173)
imgrect6X = pygame.image.load('assets/X.png')
imgrect6O = pygame.image.load('assets/O.png')

rect7 = pygame.Rect(0, 426, 182, 173)
imgrect7X = pygame.image.load('assets/X.png')
imgrect7O = pygame.image.load('assets/O.png')

rect8 = pygame.Rect(202, 426, 213, 173)
imgrect8X = pygame.image.load('assets/X.png')
imgrect8O = pygame.image.load('assets/O.png')

rect9 = pygame.Rect(436, 426, 182, 173)
imgrect9X = pygame.image.load('assets/X.png')
imgrect9O = pygame.image.load('assets/O.png')



fons = pygame.image.load('assets/tauler.png')
player = True

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and player == True:
            if event.button == 1:  # Left mouse button.
                # Check if the rect collides with the mouse pos.
                if rect1.collidepoint(event.pos):
                    tauler_info[0] = 1
                    print('Casilla 1')
                if rect2.collidepoint(event.pos):
                    tauler_info[1] = 1
                    print('Casilla 2')
                if rect3.collidepoint(event.pos):
                    print('Casilla 3')
                    tauler_info[2] = 1
                if rect4.collidepoint(event.pos):
                    print('Casilla 4')
                    tauler_info[3] = 1
                if rect5.collidepoint(event.pos):
                    print('Casilla 5')
                    tauler_info[4] = 1
                if rect6.collidepoint(event.pos):
                    print('Casilla 6')
                    tauler_info[5] = 1
                if rect7.collidepoint(event.pos):
                    print('Casilla 7')
                    tauler_info[6] = 1
                if rect8.collidepoint(event.pos):
                    print('Casilla 8')
                    tauler_info[7] = 1
                if rect9.collidepoint(event.pos):
                    print('Casilla 9')
                    tauler_info[8] = 1
        pantalla.blit(fons, (0, 0))
        pygame.display.update()
