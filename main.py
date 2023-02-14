import pygame
import random
from sprites.snake import Snake
from constants import *


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SnakeHat")
clock = pygame.time.Clock()




# Game loop
# Initialize objects



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

class Jogo:
    def __init__(self, cobra, planetas):
        self.cobra = cobra
        self.planetas = planetas
    
    def atualiza_jogo(self, delta_t):
        for planeta in self.planetas:
            planeta.atualiza_aceleracao(self.planetas)
        
        self.cobra.atualiza_velocidade_posicao(self.planetas, delta_t)



cobra = Cobra(100, 100, 10, vx=10,vy=10)
planetas = [Planeta(200, 200, 10000), Planeta(100, 500, 500000), Planeta(300, 300, 1500)]
jogo = Jogo(cobra, planetas)

# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update game state
    jogo.atualiza_jogo(1/FPS)

    # Draw / render
    screen.fill(BLACK)
    for planeta in planetas:
        pygame.draw.circle(screen, WHITE, (int(planeta.x), int(planeta.y)), 10)
    cobra.draw(screen)

    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
