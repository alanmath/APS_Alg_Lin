import pygame
import random
from constants import *
from sprites.planet import Planeta
from sprites.snake import Cobra
from sprites.elephant import Elefante

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SnakeHat")
clock = pygame.time.Clock()


class Jogo:
    def __init__(self, cobra, planetas, elefante):
        self.cobra = cobra
        self.planetas = planetas
        self.elefante = elefante
        self.score = 0
        self.phase = 1
    
    def atualiza_jogo(self, delta_t):
        for planeta in self.planetas:
            planeta.atualiza_aceleracao(self.planetas)
        
        self.cobra.atualiza_velocidade_posicao(self.planetas, delta_t)
        
        # Verificar colisão com o elefante
        dx = self.elefante.x - self.cobra.x
        dy = self.elefante.y - self.cobra.y
        dist = ((dx**2 + dy**2)**0.5)
        if dist < self.elefante.radius:
            # Incrementar a pontuação e avançar para a próxima fase
            self.score += 1
            self.phase += 1
            self.cobra = Cobra(100, 100, 10, vx=10, vy=10)
            self.planetas = [Planeta(200, 200, 10000), Planeta(100, 500, 500000), Planeta(300, 300, 1500)]
            Elefante.delete(self.elefante)
            self.elefante = Elefante(random.randint(0, WIDTH), random.randint(0, HEIGHT))

    def draw(self, screen):
        screen.fill(BLACK)
        Planeta.draw(screen)
        Elefante.draw(screen)
        self.cobra.draw(screen)

        
jogo = Jogo(cobra=Cobra(100, 100, 10, vx=10, vy=10), planetas=[Planeta(200, 200, 10000), Planeta(100, 500, 500000), Planeta(300, 300, 1500)], elefante=Elefante(random.randint(0, WIDTH), random.randint(0, HEIGHT)))

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    # Atualizar o jogo
    jogo.atualiza_jogo(delta_t=1/FPS)
    
    # Desenhar o jogo
    jogo.draw(screen)
    
    pygame.display.update()