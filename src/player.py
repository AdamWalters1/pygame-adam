# Player
import pygame
import time

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
        self.damage = 0
        self.max_damage = 100
        self.last_collision_time = 0
        self.collision_cooldown = 3  # Cooldown period in seconds
        self.last_turn_time = 0
        self.turn_cooldown = 1  # Cooldown period in seconds between turns


    def move(self, keys):
        if keys[pygame.K_UP]:
            self.current_speed = self.speed
        elif keys[pygame.K_DOWN]:
            self.current_speed = -self.speed
        else:
            self.current_speed = 0
        if keys[pygame.K_LEFT] and time.time() - self.last_turn_time > self.turn_cooldown:
            self.angle = (self.angle - 90) % 360
            self.last_turn_time = time.time()
        elif keys[pygame.K_RIGHT] and time.time() - self.last_turn_time > self.turn_cooldown:
            self.angle = (self.angle + 90) % 360
            self.last_turn_time = time.time()

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

        self.x = max(0, min(self.x, 1200 - self.size))
        self.y = max(0, min(self.y, 750 - self.size))

    def draw(self, surface):
        car_image = self.car_images[self.direction-1]
        surface.blit(car_image, (self.x, self.y))

    def check_collision(self, obstacles, obstacle_cars):
        # Check collision with obstacles
        for obstacle in obstacles:
            if self.rect.colliderect(obstacle.rect):
                if time.time() - self.last_collision_time > self.collision_cooldown:
                    self.damage += 10
                    self.last_collision_time = time.time()
                    break

        # Check collision with obstacle cars
        for obstacle_car in obstacle_cars:
            if self.rect.colliderect(obstacle_car.rect):
                if time.time() - self.last_collision_time > self.collision_cooldown:
                    self.damage += 20
                    self.last_collision_time = time.time()
                    break

    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)
