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
                # Incrementar a pontuação e avançar para a próxima fase
                self.score += 1
                self.phase += 1
                Planeta.delete_all()
                Cobra.delete_all()
                for valores in p_fases[self.phase-1]:
                    Planeta(valores)
                Elefante.delete_all()
                Elefante(e_fases[self.phase-1])
                Wormhole.delete_all()
                for valores in w_fases[self.phase-1]:
                    Wormhole(valores)  
        
        # Verificar colisão com o wormhole
        Wormhole.teletransport()

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
        text_lose = font.render("Game Over", True, WHITE)
        text_win = font.render("You Win", True, WHITE)
        
        text_rect = text_win.get_rect(center=(WIDTH/2, 200))
        
        if Core.conta_vidas <5:
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                self.screen.fill(BLACK)
                self.screen.blit(text_win, text_rect)
                pygame.display.update()
        else:
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                self.screen.fill(BLACK)
                self.screen.blit(text_lose, text_rect)
                pygame.display.update()


    def menu_screen(self):


        font = pygame.font.Font(None, 72)
        start_text = font.render("Start", True, WHITE)
        settings_text = font.render("Settings", True, WHITE)
        endless_text = font.render("Endless Mode", True, WHITE)
        start_rect = start_text.get_rect(center=(WIDTH/2, 250))
        settings_rect = settings_text.get_rect(center=(WIDTH/2, 350))
        endless_rect = endless_text.get_rect(center=(WIDTH/2, 450))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                # verificar se o rato está em cima de um botão e colocar a imagem card_menu por tras
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
                        settings_text = font.render("Settings", True, RED)
                    else:
                        settings_text = font.render("Settings", True, WHITE)
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
        Elefante(random.randint(0, WIDTH), random.randint(0, HEIGHT))
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
                # Incrementar a pontuação e avançar para a próxima fase
                self.score += 1
                self.phase += 1
                Planeta.delete_all()
                # generate the random values for the planets
                qtd_planetas = random.randint(2, 5)
                for i in range(qtd_planetas):
                    valores = [random.randint(0, WIDTH), random.randint(0, HEIGHT), random.randint(10, 50000000)]
                    Planeta(valores)
                Elefante.delete_all()
                Elefante(random.randint(0, WIDTH), random.randint(0, HEIGHT))
                qtd_wormholes = random.choice([0, 2])
                for i in range(qtd_wormholes):
                    valores = [random.randint(0, WIDTH), random.randint(0, HEIGHT), (i+1)%2]
                    Wormhole(valores)
                Wormhole.delete_all()
                
        
        # Verificar colisão com o wormhole
        Wormhole.teletransport()
        





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

                # verificar se o rato está em cima de um botão e colocar a imagem card_menu por tras
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










    

    # Define the settings page function
    def settings(self):  ## Revisar essa seção inteira ##
        # Set up the font
        font = pygame.font.SysFont('Arial', 36)

        # Set up the text labels
        title_label = font.render('Settings', True, (0, 0, 0))
        resolution_label = font.render('Resolution', True, (0, 0, 0))
        fps_label = font.render('FPS', True, (0, 0, 0))

        # Set up the resolution options
        resolution_options = [
            (320, 240),
            (640, 480),
            (800, 600),
            (1024, 768),
            (1280, 720)
        ]
        resolution_index = 2
        resolution_button_labels = [
            font.render(f'{w}x{h}', True, (0, 0, 0))
            for w, h in resolution_options
        ]

        # Set up the FPS options
        fps_options = [30, 60, 120]
        fps_index = 1
        fps_button_labels = [
            font.render(str(fps), True, (0, 0, 0))
            for fps in fps_options
        ]

        # Set up the buttons
        back_button_label = font.render('Back', True, (0, 0, 0))
        apply_button_label = font.render('Apply', True, (0, 0, 0))

        # Set up the button positions
        button_padding = 20
        button_height = back_button_label.get_height() + button_padding
        button_width = max(back_button_label.get_width(), apply_button_label.get_width())
        button_x = (WINDOW_SIZE[0] - button_width) // 2
        back_button_y = WINDOW_SIZE[1] - button_padding - button_height
        apply_button_y = back_button_y - button_height - button_padding

        # Set up the resolution button positions
        resolution_button_padding = 10
        resolution_button_height = resolution_button_labels[0].get_height() + resolution_button_padding
        resolution_button_width = max(label.get_width() for label in resolution_button_labels)
        resolution_button_x = (WINDOW_SIZE[0] - resolution_button_width) // 2
        resolution_button_y = (WINDOW_SIZE[1] - resolution_button_height * len(resolution_button_labels)) // 2

        # Set up the FPS button positions
        fps_button_padding = 10
        fps_button_height = fps_button_labels[0].get_height() + fps_button_padding
        fps_button_width = max(label.get_width() for label in fps_button_labels)
        fps_button_x = (WINDOW_SIZE[0] - fps_button_width) // 2
        fps_button_y = resolution_button_y - fps_button_padding - fps_button_height * len(fps_button_labels)
        # Loop until the user closes the settings page
        while True:
            # Draw the background
            self.screen.fill(BACKGROUND_COLOR)

            # Draw the title label
            self.screen.blit(title_label, ((WINDOW_SIZE[0] - title_label.get_width()) // 2, 50))

            # Draw the resolution label
            self.screen.blit(resolution_label, (resolution_button_x, resolution_button_y - font.get_height()))

            # Draw the resolution buttons
            for i, (w, h) in enumerate(resolution_options):
                label = font.render(f'{w}x{h}', True, (0, 0, 0))
                x = resolution_button_x
                y = resolution_button_y + i * resolution_button_height
                button_rect = pygame.Rect(x, y, resolution_button_width, resolution_button_height)
                pygame.draw.rect(self.screen, (200, 200, 200), button_rect)
                if i == resolution_index:
                    pygame.draw.rect(self.screen, (0, 0, 255), button_rect, 3)
                self.screen.blit(label, (x + (resolution_button_width - label.get_width()) // 2, y + (resolution_button_height - label.get_height()) // 2))

            # Draw the FPS label
            self.screen.blit(fps_label, (fps_button_x, fps_button_y - font.get_height()))

            # Draw the FPS buttons
            for i, fps in enumerate(fps_options):
                label = font.render(str(fps), True, (0, 0, 0))
                x = fps_button_x
                y = fps_button_y + i * fps_button_height
                button_rect = pygame.Rect(x, y, fps_button_width, fps_button_height)
                pygame.draw.rect(self.screen, (200, 200, 200), button_rect)
                if i == fps_index:
                    pygame.draw.rect(self.screen, (0, 0, 255), button_rect, 3)
                self.screen.blit(label, (x + (fps_button_width - label.get_width()) // 2, y + (fps_button_height - label.get_height()) // 2))

            # Draw the buttons
            back_button_rect = pygame.Rect(button_x, back_button_y, button_width, button_height)
            apply_button_rect = pygame.Rect(button_x, apply_button_y, button_width, button_height)
            pygame.draw.rect(self.screen, (200, 200, 200), back_button_rect)
            pygame.draw.rect(self.screen, (200, 200, 200), apply_button_rect)
            self.screen.blit(back_button_label, (button_x + (button_width - back_button_label.get_width()) // 2, back_button_y + (button_height - back_button_label.get_height()) // 2))
            self.screen.blit(apply_button_label, (button_x + (button_width - apply_button_label.get_width()) // 2, apply_button_y + (button_height - apply_button_label.get_height()) // 2))

            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # If the user clicks the close button, quit the settings page
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # If the user clicks a button, handle the click
                    mouse_pos = pygame.mouse.get_pos()
                    if back_button_rect.collidepoint(mouse_pos):
                        # If the user clicks the back button, quit the settings page
                        running = False
                    elif apply_button_rect.collidepoint(mouse_pos):
                        # If the user clicks the apply button, apply the settings and quit the settings page
                        resolution = resolution_options[resolution_index]
                        fps = fps_options[fps_index]
                        running = False