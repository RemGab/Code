# permet d'accéder aux fonctions du module pygame 
import pygame 
# Definit des couleurs RGB 
BLACK = [0, 0, 0] 
WHITE = [255, 255, 255] 
GREEN = [0, 255, 0] 
RED = [255, 0, 0] 
BLUE = [0 , 0 , 255] 
 
# initialisation de l'écran de jeu 
pygame.init() 
 
# Initialise la fenêtre de jeu 
TailleEcran = [400, 300] 
screen = pygame.display.set_mode(TailleEcran) 

pygame.quit()