import pygame
from utils import LIGHT_CYAN, RED

pygame.init()

#ekraani seaded
screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("My Screen")
screen.fill(LIGHT_CYAN)

#joonistamine
pygame.draw.line(screen, RED, [100,100], [200,200], 2)

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Close the window when clicking the "X"
            running = False

pygame.quit()