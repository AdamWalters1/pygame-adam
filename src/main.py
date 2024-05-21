# main

import pygame
from player import Player
import sys
from obstacle import Obstacle
from obstacle import ObstacleCar
import random
from random import randint
import os
# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 1000, 800
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Driving Among Idiots")

GREY = (128, 128, 128)  # RGB values for grey
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DARK_GREY = (50, 50, 50)


car_images = []
for i in range(16):
    i +=1
    car_image = pygame.image.load(f'C:/Users/adamw/OneDrive/Documents/Comp Sci/DrivingAmongIdiots-adam/assets/cars___take2/cars-{i}.png').convert_alpha()
    car_images.append(car_image)
car1 = car_images[1:4]
car2 = car_images[5:8]
car3 = car_images[13:16]
player_size = 50
player_speed = 5
player = Player(WIDTH // 2 - player_size // 2, HEIGHT // 2 - player_size // 2, player_size, player_speed, car_images)

# Define road grid
GRID_SIZE = 100  # Size of each grid square
ROAD_WIDTH = 50
NUM_ROWS = HEIGHT // GRID_SIZE
NUM_COLS = WIDTH // GRID_SIZE

# Create grid of roads
roads = []
for row in range(NUM_ROWS + 1):
    # Horizontal roads
    road_h = pygame.Rect(0, row * GRID_SIZE, WIDTH, ROAD_WIDTH)
    roads.append(road_h)
for col in range(NUM_COLS + 1):
    # Vertical roads
    road_v = pygame.Rect(col * GRID_SIZE, 0, ROAD_WIDTH, HEIGHT)
    roads.append(road_v)

# Obstacles
obstacles = [
    Obstacle(200, 300, 30, GREEN),  # Example tree
    Obstacle(400, 100, 100, BLUE),  # Example building
    Obstacle(600, 400, 20, WHITE)   # Example person
]

# Buildings as obstacles
buildings = [
    Obstacle(100, 100, 150, GREY),
    Obstacle(300, 100, 100, GREY),
    Obstacle(500, 100, 200, GREY),
    Obstacle(100, 400, 200, GREY),
    Obstacle(400, 400, 150, GREY)
]

# Create obstacle cars
obstacle_cars = [
    ObstacleCar(100, 200, 50, 3, 'horizontal', car1),
    ObstacleCar(300, 400, 50, 3, 'horizontal', car2),
    ObstacleCar(500, 100, 50, 3, 'vertical', car1),
    ObstacleCar(700, 300, 50, 3, 'vertical', car3)
]
randomnum = randint(1,2)

# Load background music and sound effects
#if randomnum == 1:  
    #background_music_path = os.path.join('..', 'assets', 'sounds', 'backgroundTraffic1.wav')
#else:
    #background_music_path = os.path.join('..', 'assets', 'sounds', 'backgroundTraffic22.wav')


#effect_path = os.path.join('..', 'assets', 'sounds', 'effect.wav')

#pygame.mixer.music.load(background_music_path)
#pygame.mixer.music.play(-1)  # Play the background music in a loop

#effect = pygame.mixer.Sound(effect_path)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.move(keys)

    #if keys[pygame.K_UP] or keys[pygame.K_DOWN] or keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
        #effect.play()
    for obstacle_car in obstacle_cars:
        obstacle_car.move()
    # background
    win.fill(WHITE)
    
    # Draw roads
    for road in roads:
        pygame.draw.rect(win, DARK_GREY, road)

    # Draw buildings
    for building in buildings:
        building.draw(win)

    for obstacle in obstacles:
        obstacle.draw(win)
        
    for obstacle_car in obstacle_cars:
        obstacle_car.draw(win)

    # Draw game objects
    player.draw(win)

    pygame.display.update()  # Update display
    pygame.time.Clock().tick(10)
    
    
# Quit Pygame
pygame.quit()
sys.exit()