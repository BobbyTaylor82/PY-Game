import pygame

# Initalize the pygame 
pygame.init()

# create the screen 
# 800 W and 600 h 
#left to right 0 --> w
# top to bottom 0 --> h
screen = pygame.display.set_mode((800,600))

# caption and icon 
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# player image 
playerImg = pygame.image.load("spaceship.png")
playerX = 370
playerY = 480

# player function 
def player(x,y):
    screen.blit(playerImg,(x,y))


# Game Loop 
running = True
while running:

    screen.fill((0,0,0))

    # quit game 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    

    player(playerX,playerY)




    pygame.display.update()
