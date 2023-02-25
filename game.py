import pygame
import random
from constants import *
from sprites.planet import Planeta
from sprites.snake import Cobra
from sprites.elephant import Elefante
from fases import *
from sprites.cannon import Canhao
from sprites.wormhole import Wormhole
from sprites.core import Core
class Jogo:
    def __init__(self, screen):
        self.score = 0
        self.phase = 1
        self.canhao = Canhao(120, HEIGHT-400)
        self.screen = screen

        #load game over screen
        self.game_over = pygame.image.load('sprites/game_over.png')



        self.background_image = pygame.image.load('sprites/background_menu.png')

        self.card_menu = pygame.image.load('sprites/card_menu.png')

        #load instructions image
        self.instructions = pygame.image.load('sprites/instrucoes.png')

        #load space image
        self.space_image = pygame.image.load('sprites/space_image.png')

        #load button menu sound named button_menu
        self.button_menu = pygame.mixer.Sound('sprites/button_menu.mp3')

    def start(self):
        for valores in p_fases[self.phase-1]:
            Planeta(valores)
        
        Elefante(e_fases[self.phase-1])
        for valores in w_fases[self.phase-1]:
            Wormhole(valores)
    
    def atualiza_jogo(self, delta_t):
        for cobra in Cobra.lista:
            cobra.atualiza_velocidade_posicao(Planeta.lista, delta_t)
        for planeta in Planeta.lista:
            cobra_ = planeta.verifica_colisao(Cobra.lista)
            if cobra_ and len(Cobra.lista)>0:
                Cobra.delete(cobra_)
                Core.incrementa_vidas()

        
        # Verificar colisão com o elefante
        for elefante in Elefante.lista:
            if elefante.verifica_colisao(Cobra.lista):
                self.next_phase(elefante)
        
        # Verificar colisão com o wormhole
        Wormhole.teletransport()

    def next_phase(self, elefante):
        if not (self.phase == 6):
            self.draw()
            pygame.display.update()
            pygame.time.delay(300)
            Cobra.delete_all()
            elefante.cobraComeu()
            self.draw()
            pygame.display.update()
            pygame.time.delay(300)
            self.score += 1
            self.phase += 1
            Planeta.delete_all()
            for valores in p_fases[self.phase-1]:
                Planeta(valores)
            Elefante.delete_all()
            Elefante(e_fases[self.phase-1])
            Wormhole.delete_all()
            for valores in w_fases[self.phase-1]:
                Wormhole(valores)

            self.draw()
        else:
            while True:
                self.screen.blit(END_GAME_IMAGE, (0, 0))
                pygame.display.update()

        
        pygame.display.update()

    def draw(self):
        self.screen.blit(self.space_image, (0, 0))

        
        Planeta.draw(self.screen)
        Elefante.draw(self.screen)
        Cobra.draw(self.screen)
        Wormhole.draw(self.screen)
        
        self.canhao.draw(self.screen)


        if Core.draw(self.screen):
            self.end_game_screen()
        


    def end_game_screen(self):
        font = pygame.font.Font(None, 36)
        text_win = font.render("You Win", True, WHITE)
        
        text_rect = text_win.get_rect(center=(WIDTH/2, 200))
        

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                            # load game over screen
            self.screen.blit(self.game_over, (0, 0))
            pygame.display.update()


    def menu_screen(self):

        font = pygame.font.Font(None, 72)
        start_text = font.render("Start", True, WHITE)
        settings_text = font.render("Instruções", True, WHITE)
        endless_text = font.render("Endless Mode", True, WHITE)
        start_rect = start_text.get_rect(center=(WIDTH/2, 250))
        settings_rect = settings_text.get_rect(center=(WIDTH/2, 350))
        endless_rect = endless_text.get_rect(center=(WIDTH/2, 450))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.MOUSEMOTION:
                    pos = pygame.mouse.get_pos()
                    if start_rect.collidepoint(pos):
                        # carregar som button_menu
                        self.button_menu.play()

                        start_text = font.render("Start", True, RED)
                    else:
                        start_text = font.render("Start", True, WHITE)
                    if settings_rect.collidepoint(pos):
                        self.button_menu.play()
                        settings_text = font.render("Instruções", True, RED)
                    else:
                        settings_text = font.render("Instruções", True, WHITE)
                    if endless_rect.collidepoint(pos):
                        self.button_menu.play()
                        endless_text = font.render("Endless Mode", True, RED)
                    else:
                        endless_text = font.render("Endless Mode", True, WHITE)

                
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if start_rect.collidepoint(pos):
                        return "start"
                    elif settings_rect.collidepoint(pos):
                        return "settings"
                    elif endless_rect.collidepoint(pos):
                        return "endless"
            
            
             # carregar background   
            self.screen.blit(self.background_image, [0, 0])


            self.screen.blit(start_text, start_rect)
            self.screen.blit(settings_text, settings_rect)
            self.screen.blit(endless_text, endless_rect)
            pygame.display.update()
    
    def endless(self):
        # generate the random values for the planets
        qtd_planetas = random.randint(2, 5)
        for i in range(qtd_planetas):
            valores = [random.randint(0, WIDTH), random.randint(0, HEIGHT), random.randint(10, 50)]
            Planeta(valores)
        # generate the random values for the elephant
        posElefante = [random.randint(0, WIDTH), random.randint(0, HEIGHT)]
        Elefante(posElefante)
        # generate the random values for the wormholes
        qtd_wormholes = random.choice([0, 2])
        for i in range(qtd_wormholes):
            valores = [random.randint(0, WIDTH), random.randint(0, HEIGHT), (i+1)%2]
            Wormhole(valores)

    def atualiza_jogo_endless(self, delta_t):
        for cobra in Cobra.lista:
            cobra.atualiza_velocidade_posicao(Planeta.lista, delta_t)
        
        # Verificar colisão com o elefante
        for elefante in Elefante.lista:
            if elefante.verifica_colisao(Cobra.lista):
                self.next_phase_endless(elefante)
                break
                
        
        # Verificar colisão com o wormhole
        Wormhole.teletransport()
        
    def next_phase_endless(self, elefante):

        self.draw()
        pygame.display.update()
        pygame.time.delay(300)
        Cobra.delete_all()
        elefante.cobraComeu()
        self.draw()
        pygame.display.update()
        pygame.time.delay(300)
        self.score += 1
        self.phase += 1
        Planeta.delete_all()
        # generate the random values for the planets
        qtd_planetas = random.randint(2, 5)
        for i in range(qtd_planetas):
            valores = [random.randint(0, WIDTH), random.randint(0, HEIGHT), random.randint(10, 50000000)]
            Planeta(valores)
        Elefante.delete_all()
        Elefante((random.randint(0, WIDTH), random.randint(0, HEIGHT)))
        qtd_wormholes = random.choice([0, 2])
        for i in range(qtd_wormholes):
            valores = [random.randint(0, WIDTH), random.randint(0, HEIGHT), (i+1)%2]
            Wormhole(valores)
        Wormhole.delete_all()




    def settings_screen(self):
        # only print the image on the sprites instrucoes as background and put a button to go back to the menu
        self.screen.blit(self.instructions, [0, 0])
        font = pygame.font.Font(None, 72)
        back_text = font.render("Back", True, WHITE)
        back_rect = back_text.get_rect(center=(WIDTH/2, 780))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.MOUSEMOTION:
                    pos = pygame.mouse.get_pos()
                    if back_rect.collidepoint(pos):
                        back_text = font.render("Back", True, RED)
                    else:
                        back_text = font.render("Back", True, WHITE)
                
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if back_rect.collidepoint(pos):
                        return "menu"
            self.screen.blit(back_text, back_rect)
            pygame.display.update()

