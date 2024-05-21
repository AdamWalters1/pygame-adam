# obstacle.py
import pygame

class Obstacle:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.rect = pygame.Rect(x, y, size, size)
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.size, self.size))

import pygame

class ObstacleCar:
    def __init__(self, x, y, size, speed, direction, car_images):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.direction = direction  # left, right, up or down
        self.car_images = car_images
        self.direction_index = 0
        self.rect = pygame.Rect(x, y, size, size)
        
        if self.direction == 'left':
            self.direction_index = 0  # Assuming index 0 for left images
        elif self.direction == 'right':
            self.direction_index = 1
        elif self.direction == 'down':
            self.direction_index = 2  # Assuming index 2 for up images
        elif self.direction == 'up':
            self.direction_index = 3

    def move(self):
        if self.direction == 'right':
            self.x += self.speed
            if self.x > 1200:  # Assuming screen width of 800, reset position
                self.x = -self.size
        elif self.direction == 'left':
            self.x -= self.speed
            if self.x < -self.size:  # Assuming screen width of 800, reset position
                self.x = 1200
        elif self.direction == 'down':
            self.y += self.speed
            if self.y > 750:  # Assuming screen height of 600, reset position
                self.y = -self.size
        elif self.direction == 'up':
            self.y -= self.speed
            if self.y < -self.size:  # Assuming screen height of 600, reset position
                self.y = 750
                
    
    def draw(self, surface):
        car_image = self.car_images[self.direction_index]
        surface.blit(car_image, (self.x, self.y))

