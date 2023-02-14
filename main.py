import pygame
import random
from sprites.snake import Snake
from constants import *

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SnakeHat")
clock = pygame.time.Clock()

# Game loop
running = True
snake = Snake(100, 100, 10, 10, GREEN)
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update
    snake.update()

    # Draw / render
    screen.fill(BLACK)
    snake.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()