# main

import pygame
from player import Player
import sys
from obstacle import Obstacle
import random
from random import randint
import os
# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Driving Among Idiots")

GREY = (128, 128, 128)  # RGB values for grey
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DARK_GREY = (50, 50, 50)

player_size = 50
player_speed = 5
player = Player(WIDTH // 2 - player_size // 2, HEIGHT // 2 - player_size // 2, player_size, player_speed)

# Obstacles
obstacles = [
    Obstacle(200, 300, 30, GREEN),  # Example tree
    Obstacle(400, 100, 100, RED),  # Example building
    Obstacle(600, 400, 20, WHITE)   # Example person
]

# Buildings as obstacles
buildings = [
    Obstacle(100, 100, 150, DARK_GREY),
    Obstacle(300, 100, 100, DARK_GREY),
    Obstacle(500, 100, 200, DARK_GREY),
    Obstacle(100, 400, 200, DARK_GREY),
    Obstacle(400, 400, 150, DARK_GREY)
]

# Roads
roads = [
    pygame.Rect(0, 250, WIDTH, 100),  # Horizontal road
    pygame.Rect(350, 0, 100, HEIGHT)  # Vertical road
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

    # background
    win.fill(GREY)
    
    # Draw roads
    for road in roads:
        pygame.draw.rect(win, WHITE, road)

    # Draw buildings
    for building in buildings:
        building.draw(win)

    for obstacle in obstacles:
        obstacle.draw(win)

    # Draw game objects
    player.draw(win)

    pygame.display.update()  # Update display
    pygame.time.Clock().tick(60)
    
    
# Quit Pygame
pygame.quit()
sys.exit()