import pygame
from utils import WHITE, BLACK, ORANGE

pygame.init()

screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Lumememm - R.Luik")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Close the window when clicking the "X"
            running = False

    screen.fill(BLACK)

    # Snowman body
    pygame.draw.circle(screen, WHITE, (150, 75), 35)
    pygame.draw.circle(screen, WHITE, (150, 145), 45)
    pygame.draw.circle(screen, WHITE, (150, 230), 55)

    # Eyes
    pygame.draw.circle(screen, BLACK, (137, 70), 6)
    pygame.draw.circle(screen, BLACK, (163, 70), 6)

    # Nose (Triangle)
    nose_points = [(145, 85), (150, 100), (155, 85)]
    pygame.draw.polygon(screen, ORANGE, nose_points)

    pygame.display.flip()

pygame.quit()