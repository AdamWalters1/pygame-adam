# main

import pygame
from player import Player
import sys
from obstacle import Obstacle
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

player_size = 50
player_speed = 5
player = Player(WIDTH // 2 - player_size // 2, HEIGHT // 2 - player_size // 2, player_size, player_speed)

# Obstacles
obstacles = [
    Obstacle(200, 300, 30, GREEN),  # Example tree
    Obstacle(400, 100, 100, RED),  # Example building
    Obstacle(600, 400, 20, WHITE)   # Example person
]

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.move(keys)

    
    # background
    win.fill(GREY)

    for obstacle in obstacles:
        obstacle.draw(win)

    # Draw game objects
    player.draw(win)

    pygame.display.update()  # Update display
    pygame.time.Clock().tick(60)
# Quit Pygame
pygame.quit()
sys.exit()