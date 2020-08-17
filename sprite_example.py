# Pygame skeleton for a new game
import pygame
import random
import os

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

# set up assets
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

class Player(pygame.sprite.Sprite):
    # sprite for the player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.Surface((50, 50))
        # self.image.fill(GREEN)
        # load player image
        self.image = pygame.image.load(os.path.join(img_folder, "p1_jump.png")).convert()
        self.image.set_colorkey(BLACK)
        # Create a rect in the size of image - rect is accually the interacting object on the game
        self.rect = self.image.get_rect()
        self.rect.center = (round(WIDTH / 2), round(HEIGHT /2))
        self.y_speed = 5

    def update(self):
        self.rect.x += 5
        # Important, when adding to Y axis, things go down on screen in pygame
        self.rect.y += self.y_speed
        # stop from going out of screen
        if self.rect.left > WIDTH:
            self.rect.right = 0
        # Set the player between y axis of 200-400, switching y_speed
        if self.rect.bottom > HEIGHT - 200:
            self.y_speed = -5
        elif self.rect.top < 200:
            self.y_speed = 5

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
    screen.fill(BLUE)
    all_sprites.draw(screen)
    # After drawing everything, flip the display to show it on screen
    pygame.display.flip()

pygame.quit()