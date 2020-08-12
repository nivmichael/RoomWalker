# Pygame skeleton for a new game
import pygame
import random

# Window Settings
WIDTH = 360
HEIGHT = 480
FPS = 30

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Init game, sound, screen, clock & caption
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
# Set clock, keeps track of the amount of time the game lapsed, and a few useful objects
clock = pygame.time.Clock()

# Game Loop
running = True
while running:
    # keep loop running at the right speed, even if the loop runs the code faster than FPS,clock will pause to keep beat
    clock.tick(FPS)
    # Process input (events) - pygame keeps track of events, even in the previous loop block
    for event in pygame.event.get():
        # Check for closing the window
        if event.type == pygame.QUIT:
            running = False
    # update
    # draw / render
    screen.fill(BLACK)
    # After drawing everything, flip the display to show it on screen
    pygame.display.flip()

pygame.quit()