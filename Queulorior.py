#https://pydefis.callicode.fr/defis/Queulorior/txt
from operator import truediv
import pygame as pg
from pygame.locals import *

pg.init()

# Génération de la fenetre
pg.display.set_caption("Queulorior")             # Définir le titre de la fenetre 
height = 500
widht = 500
screen = pg.display.set_mode((widht,height))   #Dimensions de la fenetre
screen.fill([000,000,000])


instruction = "NNEESOOEES"










pg.display.flip()

run = True 
while run: #Tant que run = true le jeu marche


    for event in pg.event.get():   # dans la liste des evenements .get
        if event.type == pg.QUIT:   # si l'evenement pg.QUIT est activé
            run = False             # on arrete le jeu
            pg.quit                 # et on quitte pygame
