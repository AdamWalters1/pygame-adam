import pygame

class Obstacle:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.size, self.size))

import pygame

class ObstacleCar:
    def __init__(self, x, y, size, speed, direction, car_images):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.direction = direction  # 'horizontal' or 'vertical'
        self.car_images = car_images
        self.direction_index = 0

        if self.direction == 'horizontal':
            self.direction_index = 0  # Assuming index 0 for horizontal images
        elif self.direction == 'vertical':
            self.direction_index = 2  # Assuming index 2 for vertical images

    def move(self):
        if self.direction == 'horizontal':
            self.x += self.speed
            if self.x > 1000:  # Assuming screen width of 800, reset position
                self.x = -self.size
        elif self.direction == 'vertical':
            self.y += self.speed
            if self.y > 800:  # Assuming screen height of 600, reset position
                self.y = -self.size

    def draw(self, surface):
        car_image = self.car_images[self.direction_index]
        surface.blit(car_image, (self.x, self.y))
