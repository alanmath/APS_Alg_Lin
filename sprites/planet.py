from sprites.corpoCeleste import CorpoCeleste
import pygame
from constants import *

class Planeta(CorpoCeleste):
    lista = []

    # def __init__(self, x, y, massa):
    #     super().__init__(x, y, massa)
    #     self.radius = 20
    #     Planeta.lista.append(self)

    def __init__(self, valores):
        super().__init__(valores[0], valores[1], valores[2])
        Planeta.lista.append(self)
        self.radius = RAIO_PLANETA
        # load planet images
        self.planeta = pygame.image.load("sprites/planet.png")

    def verifica_colisao(self, cobras):
        for cobra in cobras:
            dx = self.x - cobra.x
            dy = self.y - cobra.y
            dist = ((dx**2 + dy**2)**0.5)
            if dist < self.radius:
                return cobra
        return None

        
    @classmethod
    def listar(cls):
        return Planeta.lista

    @classmethod
    def delete_all(cls):
        Planeta.lista = []

    @classmethod
    def draw(cls, screen):
        for planeta in Planeta.lista:
            #draw planet
            screen.blit(planeta.planeta, (planeta.x, planeta.y))
            