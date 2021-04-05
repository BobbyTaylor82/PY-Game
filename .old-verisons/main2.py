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
playerX_change = 0





# player function 
def player(x,y):
    screen.blit(playerImg,(x,y))


# Game Loop 
running = True
while running:
    # RGB 
    # from 0 to 255 
    screen.fill((0,0,0))

    

    # quit game 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # if key stroke is press check whether right or left

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_change = -0.3
            # print("left arrow is pressed")
        if event.key == pygame.K_RIGHT:
            playerX_change = 0.3
            # print("right arrow is pressed")

    if event.type == pygame.KEYUP:
         if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
             playerX_change = 0
            #  print("keystoke has been released")

        
    playerX += playerX_change

    print("playerX", playerX)

    if playerX <= 0:
        playerX = 0
        print("to far left")
    elif playerX >= 500:
        playerX = 600
        print("too far right")

    player(playerX,playerY)



    pygame.display.update()
