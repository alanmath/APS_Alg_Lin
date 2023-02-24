import pygame
from constants import *
from sprites.snake import Cobra

class Wormhole:
    lista = []

    def __init__(self, x, y, indice_buraco_ligado):
        self.pos = [x, y]
        self.rect = pygame.Rect(x, y, WORMHOLE_WIDTH, WORMHOLE_HEIGHT)
        self.indice = indice_buraco_ligado
        Wormhole.lista.append(self)


        # get the image of the wormhole
    def __init__(self, valores):
        self.pos = [valores[0], valores[1]]
        self.rect = pygame.Rect(valores[0], valores[1], WORMHOLE_WIDTH, WORMHOLE_HEIGHT)
        self.indice = valores[2]
        Wormhole.lista.append(self)
        self.wormhole = pygame.image.load("sprites/portal.png")

    @classmethod
    def draw(cls, screen):
        for wormhole in Wormhole.lista:
            #draw wormhole
            screen.blit(wormhole.wormhole, (wormhole.pos[0], wormhole.pos[1]))


    @classmethod
    def delete_all(cls):
        Wormhole.lista = []

    @classmethod
    def teletransport(cls):
        for wormhole in Wormhole.lista:
            for cobra in Cobra.lista:
                if wormhole.rect.colliderect(cobra.rect):
                    pos = Wormhole.lista[wormhole.indice].pos
                    pos[0] += (WORMHOLE_WIDTH + SNAKE_WIDTH + 4) / 2
                    # pos[1] += (WORMHOLE_HEIGHT + SNAKE_HEIGHT + 10) / 2
                    cobra.transportar(pos)
