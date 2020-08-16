# Pygame skeleton for a new game
import pygame
import random

# Window Settings
WIDTH = 800
HEIGHT = 600
FPS = 30

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Player(pygame.sprite.Sprite):
    # sprite for the player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (round(WIDTH / 2), round(HEIGHT /2))

    def update(self):
        self.rect.x += 5
        # stop from going out of screen
        if self.rect.left > WIDTH:
            self.rect.right = 0

# Init game, sound, screen, clock & caption
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
# Set clock, keeps track of the amount of time the game lapsed, and a few useful objects
clock = pygame.time.Clock()

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