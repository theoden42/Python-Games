import pygame
import os
from sys import exit
ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), ".."))

def displayGame():
    running = True
    gridimagepath = os.path.join(ROOT_DIR, "res", "grid.png")
    logoimagepath = os.path.join(ROOT_DIR, "res", "logo.png")

    screen = pygame.display.set_mode((640,480))
    logoimage = pygame.image.load(logoimagepath).convert_alpha()
    pygame.display.set_caption("TikiTikiTwoTwo")
    pygame.display.set_icon(logoimage)
    gridimage = pygame.image.load(gridimagepath).convert_alpha()
    gridimage = pygame.transform.scale(gridimage, (320, 240))
    
    while running:      
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit()
        screen.fill((255,255,255))
        screen.blit(gridimage,(0,0))
        pygame.display.update()
        



    

if __name__ == "__main__":
    pygame.init()
    displayGame()