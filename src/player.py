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

    

    def move(self, keys, obstacles, obstacle_cars):
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

        new_x = self.x
        new_y = self.y
        
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
        
        new_rect = pygame.Rect(new_x, new_y, self.size, self.size)

        for obstacle in obstacles:
            if new_rect.colliderect(obstacle.rect):
                self.x, self.y = self.avoid_collision(new_x, new_y, obstacle.rect)

        # Check collision with obstacle cars
        for obstacle_car in obstacle_cars:
            if new_rect.colliderect(obstacle_car.rect):
                self.x, self.y = self.avoid_collision(new_x, new_y, obstacle_car.rect)

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
                    obstacle_car.crashed = True
                    
                    break
                
    def avoid_collision(self, new_x, new_y, obstacle_rect):
        # Calculate the distance between the player and the obstacle
        dx = obstacle_rect.centerx - new_x
        dy = obstacle_rect.centery - new_y

        # Move the player away from the obstacle along the shortest axis
        if abs(dx) > abs(dy):
            new_x -= dx / abs(dx) * self.speed
        else:
            new_y -= dy / abs(dy) * self.speed

        return new_x, new_y
    def spawn_new_car(self):
        # Randomly generate new coordinates for the obstacle car
        x = random.randint(0, 1200 - self.size)
        y = random.randint(0, 750 - self.size)
        return x, y
    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)
