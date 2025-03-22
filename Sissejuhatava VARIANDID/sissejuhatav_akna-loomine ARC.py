import pygame
from utils import LIGHT_CYAN, BLACK

pygame.init()

#ekraani seaded
screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("My Screen")
screen.fill(LIGHT_CYAN)

#joonistamine
pygame.draw.arc(screen, BLACK, [100,100,250,200], 0, 3.14*1.5, 1)

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Close the window when clicking the "X"
            running = False

pygame.quit()