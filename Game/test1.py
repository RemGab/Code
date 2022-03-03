# permet d'accéder aux fonctions du module pygame 
import pygame 
# Definit des couleurs RGB 
BLACK = [0, 0, 0] 
WHITE = [255, 255, 255] 
GREEN = [0, 255, 0] 
RED = [255, 0, 0] 
BLUE = [0 , 0 , 255] 
path = r'Game\ressource'
# initialisation de l'écran de jeu 
pygame.init() 

TailleEcran = [300, 200] 
ecran = pygame.display.set_mode(TailleEcran)

# pygame.display.set_caption("Mon super titre de Ouf !")

image = pygame.image.load(path + "\image.png").convert_alpha()
# pygame.display.set_icon(image)

# Initialise la fenêtre de jeu 



continuer = True

while continuer :
    ecran.blit(image,(0,50))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            continuer = False
    pygame.display.flip()
pygame.quit()