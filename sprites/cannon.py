import pygame
from constants import *
from sprites.snake import Cobra
import math
# object cannon that creates object bullet at a given angle and velocity

class Canhao():
    def __init__(self, x, y):
        self.image = pygame.Surface((20, 30))
        self.image.fill(GREEN)
        self.pos = (x, y)

        self.rect = self.image.get_rect()
        self.shoot = False
        

        #alterações de alan - linha vetorizada
        self.line_color = (255, 255, 255)
        self.line_width = 5
        self.line_length = 50

        self.pulled_back = False
        self.start_pos = [0,0]
        self.speed = [0,0]
        # Cria uma linha horizontal
        self.line_image = pygame.Surface((self.line_length, self.line_width))
        self.line_image.fill(self.line_color)


        # carregue a imagem principe
        self.prince_image = pygame.image.load("sprites/principe.png")
        
    
    def update_cannon_down(self):
        # verify if mouse button was pressed
        self.pulled_back = True
        self.start_pos = pygame.mouse.get_pos()


                
    def update_cannon_up(self):
        end_pos = pygame.mouse.get_pos()
        # calcula a distância entre os pontos
        distance = ((end_pos[0] - self.start_pos[0])**2 + (end_pos[1] - self.start_pos[1])**2)**0.5
        # calcula o ângulo entre o ponto inicial e final
        angle = math.atan2(end_pos[1] - self.start_pos[1], end_pos[0] - self.start_pos[0])
        # define a força do lançamento com base na distância
        force = min(distance, 1000)
        # define a velocidade do objeto com base na força e ângulo
        self.speed[0] = force * math.cos(angle)*(-1)
        self.speed[1] = force * math.sin(angle)*(-1)
        self.pulled_back = False
        Cobra(self.pos[0], self.pos[1], 10, vx=self.speed[0], vy=self.speed[1])


    def update_cannon_motion(self):
        self.mouse_pos = pygame.mouse.get_pos()


        
    def pulled(self, screen):
        if self.pulled_back:
            mouse_pos = pygame.mouse.get_pos()
            distance_to_color = min(((mouse_pos[0] - self.start_pos[0])**2 + (mouse_pos[1] - self.start_pos[1])**2)**0.5,255)
            pygame.draw.line(screen, (0+distance_to_color, 255-distance_to_color, 0), self.start_pos, mouse_pos, 2)
            

    def draw(self, screen):

        # desenhe o objeto principe.png na tela
        screen.blit(self.prince_image, (self.pos[0]-60, self.pos[1]-20))
