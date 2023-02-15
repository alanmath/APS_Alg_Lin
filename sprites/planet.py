from sprites.corpoCeleste import CorpoCeleste
import pygame

class Planeta(CorpoCeleste):
    lista = []

    def __init__(self, x, y, massa):
        super().__init__(x, y, massa)
        Planeta.lista.append(self)

    def __init__(self, valores):
        super().__init__(valores[0], valores[1], valores[2])
        Planeta.lista.append(self)
    
    # def atualiza_aceleracao(self, planetas):
    #     # Calcular a aceleração resultante devido à atração gravitacional dos outros planetas
    #     self.ax = 0
    #     self.ay = 0
    #     for planeta in planetas:
    #         if planeta != self:
    #             dx = planeta.x - self.x
    #             dy = planeta.y - self.y
    #             dist = ((dx**2 + dy**2)**0.5)
    #             f = self.massa * planeta.massa / dist**2
    #             self.ax += f * dx / dist
    #             self.ay += f * dy / dist

    @classmethod
    def listar(cls):
        return Planeta.lista

    @classmethod
    def delete_all(cls):
        Planeta.lista = []

    @classmethod
    def draw(cls, screen):
        for planeta in Planeta.lista:
            pygame.draw.circle(screen, (255, 255, 255), (planeta.x, planeta.y), 10)