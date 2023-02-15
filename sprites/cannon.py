import pygame
from constants import *
from sprites.snake import Cobra
import math
# object cannon that creates object bullet at a given angle and velocity

class Canhao():
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 30))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.angle = 0
        self.velocity = 1000
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.angle -= 2.5 
        elif keys[pygame.K_RIGHT]:
            self.angle += 2.5
        if keys[pygame.K_SPACE]:
            # Shoot cobra with given angle and velocity
            cobra_velocity = (self.velocity * math.cos(math.radians(self.angle)), self.velocity * math.sin(math.radians(self.angle)))
            Cobra(self.rect.centerx, self.rect.centery, 10, vx=cobra_velocity[0], vy=cobra_velocity[1])

    def draw(self, screen):
        # self.image = pygame.transform.rotate(self.image, self.angle)
        screen.blit(self.image, self.rect)