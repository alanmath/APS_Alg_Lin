import pygame
from constants import *

class Cobra:
    lista = []

    def __init__(self, x, y, massa, vx, vy):
        self.x = x
        self.y = y
        self.massa = massa
        self.vx = vx
        self.vy = vy
        self.rect = pygame.Rect(self.x, self.y, SNAKE_WIDTH, SNAKE_HEIGHT)
        Cobra.lista.append(self)
    
    def atualiza_velocidade_posicao(self, planetas, delta_t):
        # Calcular a aceleração resultante devido à atração gravitacional dos planetas
        ax = 0
        ay = 0
        for planeta in planetas:
            dx = planeta.x - self.x
            dy = planeta.y - self.y
            dist = ((dx**2 + dy**2)**0.5)
            f = self.massa * planeta.massa / dist**2
            ax += f * dx / dist
            ay += f * dy / dist
        
        # Atualizar a velocidade da cobra
        self.vx += ax * delta_t
        self.vy += ay * delta_t
        
        # Atualizar a posição da cobra
        self.x += self.vx * delta_t
        self.y += self.vy * delta_t
        
        

        self.rect = pygame.Rect(self.x, self.y, SNAKE_WIDTH, SNAKE_HEIGHT)

    def transportar(self, pos):
        self.x = pos[0]
        self.y = pos[1]
        self.rect = pygame.Rect(self.x, self.y, SNAKE_WIDTH, SNAKE_HEIGHT)

    @classmethod
    def draw(cls, screen):
        for cobra in Cobra.lista:
            pygame.draw.rect(screen, (255, 0, 0), cobra.rect)

    @classmethod
    def delete(cls, cobra):
        Cobra.lista.remove(cobra)

    @classmethod
    def delete_all(cls):
        Cobra.lista = []

    @classmethod
    def listar(cls):
        return Cobra.lista
