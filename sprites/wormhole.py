import pygame
from constants import *
from sprites.snake import Cobra

class Wormhole:
    lista = []

    def __init__(self, x, y, indice_buraco_ligado):
        self.pos = (x, y)
        self.rect = pygame.Rect(x, y, WORMHOLE_WIDTH, WORMHOLE_HEIGHT)
        self.indice = indice_buraco_ligado
        Wormhole.lista.append(self)

    def __init__(self, valores):
        self.pos = (valores[0], valores[1])
        self.rect = pygame.Rect(valores[0], valores[1], WORMHOLE_WIDTH, WORMHOLE_HEIGHT)
        self.indice = valores[2]
        Wormhole.lista.append(self)
        
    @classmethod
    def draw(cls, screen):
        for wormhole in Wormhole.lista:
            pygame.draw.rect(screen, (255, 255, 255), wormhole.rect)

    @classmethod
    def delete_all(cls):
        Wormhole.lista = []

    @classmethod
    def teletransport(cls):
        for wormhole in Wormhole.lista:
            for cobra in Cobra.lista:
                if wormhole.rect.colliderect(cobra.rect):
                    cobra.transportar(Wormhole.lista[wormhole.indice].pos)
