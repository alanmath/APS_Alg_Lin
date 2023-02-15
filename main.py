import pygame
import random
from constants import *
from sprites.planet import Planeta
from sprites.snake import Cobra
from sprites.elephant import Elefante
from fases import *

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SnakeHat")
clock = pygame.time.Clock()


class Jogo:
    def __init__(self):
        self.score = 0
        self.phase = 1

    def start(self):
        for valores in p_fases[self.phase-1]:
            Planeta(valores)
        Elefante(random.randint(0, WIDTH), random.randint(0, HEIGHT))
    
    def atualiza_jogo(self, delta_t):
        for cobra in Cobra.lista:
            cobra.atualiza_velocidade_posicao(Planeta.lista, delta_t)
        
        # Verificar colisão com o elefante
        for elefante in Elefante.lista:
            if elefante.verifica_colisao(Cobra.lista):
                # Incrementar a pontuação e avançar para a próxima fase
                self.score += 1
                self.phase += 1
                Planeta.delete_all()
                for valores in p_fases[self.phase-1]:
                    Planeta(valores)
                Elefante.delete_all()
                Elefante(random.randint(0, WIDTH), random.randint(0, HEIGHT))

    def draw(self, screen):
        screen.fill(BLACK)
        Planeta.draw(screen)
        Elefante.draw(screen)
        Cobra.draw(screen)

    def menu_screen(self):
        font = pygame.font.Font(None, 36)
        start_text = font.render("Start", True, WHITE)
        settings_text = font.render("Settings", True, WHITE)
        endless_text = font.render("Endless Mode", True, WHITE)
        start_rect = start_text.get_rect(center=(WIDTH/2, 200))
        settings_rect = settings_text.get_rect(center=(WIDTH/2, 250))
        endless_rect = endless_text.get_rect(center=(WIDTH/2, 300))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if start_rect.collidepoint(pos):
                        return "start"
                    elif settings_rect.collidepoint(pos):
                        return "settings"
                    elif endless_rect.collidepoint(pos):
                        return "endless"
            
            screen.fill(BLACK)
            screen.blit(start_text, start_rect)
            screen.blit(settings_text, settings_rect)
            screen.blit(endless_text, endless_rect)
            pygame.display.update()

        
jogo = Jogo()
jogo.menu_screen()
jogo.start()

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