import pygame
from utils import LIGHT_CYAN, MAGENTA

pygame.init()

#ekraani seaded
screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("My Screen")
screen.fill(LIGHT_CYAN)

#joonistamine
pygame.draw.polygon(screen, MAGENTA, [[50,50],[100,50],[100,150],[250,50],[350,250],[50,250]], 2)

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Close the window when clicking the "X"
            running = False

pygame.quit()