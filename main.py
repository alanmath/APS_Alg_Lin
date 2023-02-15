import pygame
from game import Jogo
from constants import *

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SnakeHat")
clock = pygame.time.Clock()

        
jogo = Jogo(screen)
while True:
    retorno_menu = jogo.menu_screen() 
    if retorno_menu == "start":
        jogo.start()

        while True:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            # Atualizar o jogo
                if event.type == pygame.KEYDOWN:
                    jogo.canhao.update()

            jogo.atualiza_jogo(delta_t=1/FPS)
            
            # Desenhar o jogo
            jogo.draw()
            
            pygame.display.update()

    elif retorno_menu == "endless":
        jogo.endless()
        while True:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            # Atualizar o jogo
                if event.type == pygame.KEYDOWN:
                    jogo.canhao.update()
                if event.type == pygame.KEYUP:
                    jogo.canhao.release()

            jogo.atualiza_jogo_endless(delta_t=1/FPS)
            
            # Desenhar o jogo
            jogo.draw()
            
            pygame.display.update()

    elif retorno_menu == "settings":
        print("settings")