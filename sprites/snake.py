import pygame


class Cobra:
    def __init__(self, x, y, massa, vx, vy):
        self.x = x
        self.y = y
        self.massa = massa
        self.vx = vx
        self.vy = vy
    
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

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, 10, 10))
