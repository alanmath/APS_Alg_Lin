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
        self.last_space_press_time = 0
        self.barra_carregamento = pygame.Surface((100, 10))
        self.barra_carregamento.fill(RED)
        self.rect_barra = self.barra_carregamento.get_rect()
        self.rect_barra.center = (x, y + 50)
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.angle -= 2.5 
        elif keys[pygame.K_RIGHT]:
            self.angle += 2.5
        elif keys[pygame.K_SPACE]:
            # Shoot cobra with given angle and velocity
            current_time = pygame.time.get_ticks()
            time_since_press = current_time - self.last_space_press_time

            # Calculate velocity based on time held down
            self.velocity = max(0, min(1000, time_since_press * 2))
            self.update_barra(self.velocity/10)
            cobra_velocity = (self.velocity * math.cos(math.radians(self.angle)), self.velocity * math.sin(math.radians(self.angle)))
            Cobra(self.rect.centerx, self.rect.centery, 10, vx=cobra_velocity[0], vy=cobra_velocity[1])
    
    def update_barra(self, percentage):
        self.barra_carregamento = pygame.Surface((percentage, 10))
        self.barra_carregamento.fill(RED)
        self.rect_barra = self.barra_carregamento.get_rect()
        self.rect_barra.center = (self.rect.centerx, self.rect.centery + 50)

    def release(self):
        self.last_space_press_time = pygame.time.get_ticks()

    def draw(self, screen):
        # self.image = pygame.transform.rotate(self.image, self.angle)
        screen.blit(self.image, self.rect)
        screen.blit(self.barra_carregamento, self.rect_barra)