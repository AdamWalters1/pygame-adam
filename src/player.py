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
        self.current_speed = 0
        self.angle = 0  # Angle in degrees (0, 90, 180, 270)
        
    def move(self, keys):
        
        if keys[pygame.K_UP]:
            self.current_speed = self.speed
        elif keys[pygame.K_DOWN]:
            self.current_speed = -self.speed
        else:
            self.current_speed = 0
        if keys[pygame.K_LEFT]:
            self.angle = (self.angle - 90) % 360
        elif keys[pygame.K_RIGHT]:
            self.angle = (self.angle + 90) % 360

        if self.angle == 0:
            self.y += self.current_speed
            self.direction = 11
        elif self.angle == 90:
            self.x += self.current_speed
            self.direction = 10
        elif self.angle == 180:
            self.y -= self.current_speed
            self.direction = 12
        elif self.angle == 270:
            self.x -= self.current_speed
            self.direction = 9


    def draw(self, surface):
        car_image = self.car_images[self.direction-1]
        surface.blit(car_image, (self.x, self.y))
    