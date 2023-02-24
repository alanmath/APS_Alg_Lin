import pygame
from constants import *
from sprites.snake import Cobra

## class of the target sprite Elephant
class Elefante:
    lista = []

    def __init__(self, pos):
        self.x = pos[0]
        self.y = pos[1]
        self.radius = ELEPHANT_RADIUS
        self.image = ELEPHANT_IMAGE
        Elefante.lista.append(self)

    def verifica_colisao(self, cobras):
        for cobra in cobraspygame.time.delay(300):
            dx = self.x - cobra.x
            dy = self.y - cobra.y
            dist = ((dx**2 + dy**2)**0.5)
            if dist < self.radius:
                cobra.abrir_boca()
                return True
        return False

    def cobraComeu(self):
        self.image = SNAKE_WHO_EAT_ELEPHANT_IMAGE

    def getPosition(self):
        return (self.x, self.y)

    @classmethod
    def listar(cls):
        return Elefante.lista
    
    @classmethod
    def draw(cls, screen):
        for elefante in Elefante.lista:
            # pygame.draw.circle(screen, ELEPHANT_COLOR, (elefante.x, elefante.y), elefante.radius)
            screen.blit(elefante.image, (elefante.x, elefante.y))

    @classmethod
    def delete(cls, elefante):
        Elefante.lista.remove(elefante)

    @classmethod
    def delete_all(cls):
        Elefante.lista = []


