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
        Elefante.lista.append(self)

        # get the image of the elephant 
        self.elefante = pygame.image.load("sprites/elephant.png")

    def verifica_colisao(self, cobras):
        for cobra in cobras:
            dx = self.x - cobra.x
            dy = self.y - cobra.y
            dist = ((dx**2 + dy**2)**0.5)
            if dist < self.radius:
                Cobra.delete(cobra)
                return True
        return False

    @classmethod
    def listar(cls):
        return Elefante.lista
    
    @classmethod
    def draw(cls, screen):
        for elefante in Elefante.lista:
            #draw elefante
            screen.blit(elefante.elefante, (elefante.x, elefante.y))
    @classmethod
    def delete(cls, elefante):
        Elefante.lista.remove(elefante)

    @classmethod
    def delete_all(cls):
        Elefante.lista = []


