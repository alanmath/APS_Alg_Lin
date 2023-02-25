import pygame

WIDTH = 1600
HEIGHT = 900
FPS = 60

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

## whormhole
WORMHOLE_HEIGHT = 60
WORMHOLE_WIDTH = 10
WORMHOLE_COLOR = BLUE

## PLANETA
RAIO_PLANETA = 22

## snake
SNAKE_COLOR = RED
SNAKE_WIDTH = 20
SNAKE_HEIGHT = 20

## elephant
ELEPHANT_COLOR = YELLOW
ELEPHANT_RADIUS = 35

## elephant images
ELEPHANT_IMAGE = pygame.image.load('sprites/elephant.png')
ELEPHANT_IMAGE = pygame.transform.scale(ELEPHANT_IMAGE, (ELEPHANT_RADIUS*2, ELEPHANT_RADIUS*2))

## snake images
SNAKE_IMAGE = pygame.image.load('sprites/cobra.png')
SNAKE_IMAGE = pygame.transform.scale(SNAKE_IMAGE, (SNAKE_WIDTH, SNAKE_HEIGHT))
SNAKE_IMAGE_OPEN_MOUTH = pygame.image.load('sprites/mouth_snake.png')
SNAKE_IMAGE_OPEN_MOUTH = pygame.transform.scale(SNAKE_IMAGE_OPEN_MOUTH, (SNAKE_WIDTH, SNAKE_HEIGHT))
SNAKE_WHO_EAT_ELEPHANT_IMAGE = pygame.image.load('sprites/snakehat_image.png')
SNAKE_WHO_EAT_ELEPHANT_IMAGE = pygame.transform.scale(SNAKE_WHO_EAT_ELEPHANT_IMAGE, (ELEPHANT_RADIUS, ELEPHANT_RADIUS))


##
END_GAME_IMAGE = pygame.image.load('sprites/endgame.png')

# Settings page
WINDOW_SIZE = (800, 600)
FPS = 60
BACKGROUND_COLOR = (255, 255, 255)
