import pygame

## class of the target sprite Elephant
class Elefante:
    lista = []

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 15
        Elefante.lista.append(self)
    
    @classmethod
    def draw(cls, screen):
        for elefante in Elefante.lista:
            pygame.draw.circle(screen, (0, 255, 0), (elefante.x, elefante.y), elefante.radius)

    @classmethod
    def delete(cls, elefante):
        Elefante.lista.remove(elefante)


