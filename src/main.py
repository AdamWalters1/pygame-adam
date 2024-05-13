# main

import pygame
from player import Player

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")

# Create player
player = Player(WIDTH//2, HEIGHT//2)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.move(keys)

    # Game logic (score, game over condition, etc.)

    # Update display
    win.fill((0, 0, 0))  # Clear screen
    # Draw game objects
    pygame.draw.rect(win, (255, 0, 0), (player.x, player.y, 50, 50))  # Example: drawing player as a red rectangle
    pygame.display.update()  # Update display

# Quit Pygame
pygame.quit()