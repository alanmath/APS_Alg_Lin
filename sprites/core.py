import pygame
from sprites.snake import Cobra
from constants import *

class Core:
    conta_vidas = 0
    posicoes = [(450,50),(500,50),(550,50),(600,50),(650,50)]
        
    coracao_preenchido = pygame.image.load("sprites/preenchido.png")
    coracao_vazio = pygame.image.load("sprites/vazio.png")


    def __init__(self):
        
        pass
        # coracao_preenchido = pygame.image.load("preenchido.png")
        # coracao_vazio = pygame.image.load("vazio.png")

    @classmethod
    def update_vidas(self):
        #verify if a snake in the snake list is out of the screen
        for snake in Cobra.lista:
            #verify if the snake is out of the screen
            if snake.x < 0 or snake.x > WIDTH or snake.y < 0 or snake.y > HEIGHT:
                #delete the snake
                Cobra.delete(snake)
                #add 1 to the self.conta_vidas
                Core.conta_vidas += 1
                #verify if the self.conta_vidas is 5
                if Core.conta_vidas == 5:
                    return True
        return False
                    #call the function game_over

    @classmethod           
    def incrementa_vidas(self):
        self.conta_vidas += 1     

    @classmethod
    def draw(cls,screen):
        if cls.conta_vidas == 0:
            #draw the image preenchido.png on the positions self.posicoes, 5 times
            for posicao in cls.posicoes:
                screen.blit(cls.coracao_preenchido, posicao)
            
        elif cls.conta_vidas == 1:
            #draw the image preenchido.png on the positions self.posicoes, 4 times
            for posicao in cls.posicoes[1:]:
                screen.blit(cls.coracao_preenchido, posicao)

            for posicao in cls.posicoes[:1]:
                screen.blit(cls.coracao_vazio, posicao)

        elif cls.conta_vidas == 2:
            #draw the image preenchido.png on the positions self.posicoes, 3 times
            for posicao in cls.posicoes[2:]:
                screen.blit(cls.coracao_preenchido, posicao)
            for posicao in cls.posicoes[:2]:
                screen.blit(cls.coracao_vazio, posicao)

        elif cls.conta_vidas == 3:
            #draw the image preenchido.png on the positions self.posicoes, 2 times
            for posicao in cls.posicoes[3:]:
                screen.blit(cls.coracao_preenchido, posicao)
            for posicao in cls.posicoes[:3]:
                screen.blit(cls.coracao_vazio, posicao)

        elif cls.conta_vidas == 4:
            #draw the image preenchido.png on the positions self.posicoes, 1 times
            for posicao in cls.posicoes[4:]:
                screen.blit(cls.coracao_preenchido, posicao)
            for posicao in cls.posicoes[:4]:
                screen.blit(cls.coracao_vazio, posicao)

        elif cls.conta_vidas == 5:
            #draw the image preenchido.png on the positions self.posicoes, 0 times

            for posicao in cls.posicoes:
                screen.blit(cls.coracao_vazio, posicao)