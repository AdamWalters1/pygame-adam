# Player

import pygame

class Player:
    def __init__(self, x, y, size, speed, car_images):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed

    def move(self, keys):
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed

    def draw(self, surface):
        car_image = self.car_images[self.direction]
        surface.blit(car_image, (self.x, self.y))
    #def draw(self, surface):
        #pygame.draw.rect(surface, (255, 0, 0), (self.x, self.y, self.size, self.size))