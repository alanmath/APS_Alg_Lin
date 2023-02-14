import pygame

# projectile class
class Snake(pygame.sprite.Sprite):
    Snakes = []

    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.change_x = 5
        self.change_y = 5
        Snake.Snakes.append(self)

    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y

    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)