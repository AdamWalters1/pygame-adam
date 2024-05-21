# Player

import pygame

class Player:
    def __init__(self, x, y, size, speed, car_images):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.car_images = car_images
        self.direction = 1
    def move(self, keys):
        if keys[pygame.K_UP]:
            self.y -= self.speed
            self.direction = 11
        if keys[pygame.K_DOWN]:
            self.y += self.speed
            self.direction = 12
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
            self.direction = 9
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
            self.direction = 10

    def draw(self, surface):
        car_image = self.car_images[self.direction-1]
        surface.blit(car_image, (self.x, self.y))
    #def draw(self, surface):
        #pygame.draw.rect(surface, (255, 0, 0), (self.x, self.y, self.size, self.size))