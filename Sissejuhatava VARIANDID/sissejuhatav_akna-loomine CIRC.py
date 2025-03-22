import pygame
from utils import LIGHT_CYAN, BLUE

pygame.init()

#ekraani seaded
screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("My Screen")
screen.fill(LIGHT_CYAN)

#joonistamine
pygame.draw.circle(screen, BLUE, [150,200], 100, 1)

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Close the window when clicking the "X"
            running = False

pygame.quit()