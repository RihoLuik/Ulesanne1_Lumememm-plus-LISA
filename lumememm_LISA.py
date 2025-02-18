import pygame
import math # Import math for cos() and sin()
from utils import WHITE, BLACK, ORANGE, LIGHT_BLUE, GRAY, YELLOW, SUN_CENTER, SUN_RADIUS, BROWN

pygame.init()

screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Lumememm - R.Luik")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Close the window when clicking the "X"
            running = False

    screen.fill(LIGHT_BLUE)

    # THE SUN
    pygame.draw.circle(screen, YELLOW, SUN_CENTER, SUN_RADIUS)

    # THE RAYS OF THE ALMIGHTY SUN
    ray_length = 70 # How far the rays extend
    for angle in range(0, 360, 30):
        radians = math.radians(angle)
        x_end = SUN_CENTER[0] + ray_length * math.cos(radians)
        y_end = SUN_CENTER[1] + ray_length * math.sin(radians)
        pygame.draw.line(screen, YELLOW, SUN_CENTER, (x_end, y_end), 3) # 3px rays


    # Cloud nr. 1
    pygame.draw.circle(screen, GRAY, (70, 60), 27.5)
    pygame.draw.circle(screen, GRAY, (45, 65), 25)

    # Cloud nr. 2
    pygame.draw.circle(screen, GRAY, (160, 60), 35)
    pygame.draw.circle(screen, GRAY, (130, 65), 32.5)
    pygame.draw.circle(screen, GRAY, (190, 70), 28.5)

    # Cloud nr. 3
    pygame.draw.circle(screen, GRAY, (250, 60), 30)
    pygame.draw.circle(screen, GRAY, (275, 65), 28)

    # Snowman body
    pygame.draw.circle(screen, WHITE, (150, 75), 35) # Top
    pygame.draw.circle(screen, WHITE, (150, 145), 45) # Middle
    pygame.draw.circle(screen, WHITE, (150, 230), 55) # Bottom

    # The Sticks :) (Hands)
    pygame.draw.line(screen, BROWN, (110, 145), (60, 145), 4)
    pygame.draw.line(screen, BROWN, (190, 145), (240, 145), 4)

    # Sweep sweep
    sweep_points = [(60, 75), (90, 45), (30, 45)]
    pygame.draw.line(screen, BROWN, (60, 75), (60, 270), 3)
    pygame.draw.polygon(screen, BROWN, sweep_points)

    # Eyes
    pygame.draw.circle(screen, BLACK, (137, 70), 6)
    pygame.draw.circle(screen, BLACK, (163, 70), 6)

    # Buttons
    pygame.draw.circle(screen, BLACK, (150, 125), 5)
    pygame.draw.circle(screen, BLACK, (150, 152.5), 5)
    pygame.draw.circle(screen, BLACK, (150, 200), 5)

    # Nose (Triangle)
    nose_points = [(145, 85), (150, 100), (155, 85)]
    pygame.draw.polygon(screen, ORANGE, nose_points)

    # The Hat :D
    hat_points = [(100, 35), (100, 45), (200, 45), (200, 35), (125, 35), (125, 0), (175, 0), (175, 35), (200, 35)]
    pygame.draw.polygon(screen, BLACK, hat_points)

    pygame.display.flip()

pygame.quit()