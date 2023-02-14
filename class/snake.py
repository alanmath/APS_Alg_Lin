import pygame

class snake:
    
    def __init__(self, x, y, color, size, direction):
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.direction = direction
        self.body = []

    def draw(self, surface):
        for i in self.body:
            pygame.draw.rect(surface, self.color, (i[0], i[1], self.size, self.size))

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i] = (self.body[i - 1][0], self.body[i - 1][1])
        if self.direction == 'up':
            self.body[0] = (self.body[0][0], self.body[0][1] - self.size)
        elif self.direction == 'down':
            self.body[0] = (self.body[0][0], self.body[0][1] + self.size)
        elif self.direction == 'left':
            self.body[0] = (self.body[0][0] - self.size, self.body[0][1])
        elif self.direction == 'right':
            self.body[0] = (self.body[0][0] + self.size, self.body[0][1])

    def add(self):
        if self.direction == 'up':
            self.body.append((self.body[-1][0], self.body[-1][1] + self.size))
        elif self.direction == 'down':
            self.body.append((self.body[-1][0], self.body[-1][1] - self.size))
        elif self.direction == 'left':
            self.body.append((self.body[-1][0] + self.size, self.body[-1][1]))
        elif self.direction == 'right':
            self.body.append((self.body[-1][0] - self.size, self.body[-1][1]))

    def reset(self):
        self.body = []

    def get_head_pos(self):
        return self.body[0]

    def get_body(self):
        return self.body

    def get_direction(self):
        return self.direction

    def set_direction(self, direction):
        self.direction = direction

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def get_size(self):
        return self.size