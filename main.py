import pygame
from game import Jogo
from constants import *
from sprites.core import Core

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SnakeHat")
clock = pygame.time.Clock()

#carregar algumas imagens aqui
#carregar imagens aqui
frame_count = 0

#take music on the folder sprites and load it on the pygame mixer, the music is back_sound
pygame.mixer.music.load("sprites/back_sound.mp3")
#play the music
        
jogo = Jogo(screen)
while True:
    pygame.mixer.music.play(loops=-1)
    retorno_menu = jogo.menu_screen() 

    if retorno_menu == "start":
        jogo.start()

        while True:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    jogo.canhao.update_cannon_down()
                elif event.type == pygame.MOUSEBUTTONUP:
                    jogo.canhao.update_cannon_up()
                elif event.type == pygame.MOUSEMOTION:
                    jogo.canhao.update_cannon_motion()

            jogo.atualiza_jogo(delta_t=1/FPS)
            
            # Desenhar o jogo
            jogo.draw()
            # Desenhar linha de força
            jogo.canhao.pulled(screen)
            

            if Core.update_vidas():
                jogo.end_game_screen()

            #desenhar coracoes
            

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
        jogo.settings_screen()

        
