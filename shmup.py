# Pygame skeleton for a new game
import pygame
import random

# Window Settings
WIDTH = 480
HEIGHT = 600
FPS = 60

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
pygame.display.set_caption("Shmup!")
# Set clock, keeps track of the amount of time the game lapsed, and a few useful objects
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        # Initiate base vars to the rect object
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT -10
        self.speedx = 0
    def update(self):
        self.rect.x += self.speedx


all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
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
    all_sprites.update()
    # draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # After drawing everything, flip the display to show it on screen
    pygame.display.flip()

pygame.quit()