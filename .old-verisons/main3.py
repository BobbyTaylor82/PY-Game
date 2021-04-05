import pygame
import random
import math


# Initalize the pygame 
pygame.init()


# create the screen 
# 800 W and 600 h 
#left to right 0 --> w
# top to bottom 0 --> h
screen = pygame.display.set_mode((800,600))

# background 
bg = pygame.image.load(r"photos\galaga.png")

# caption and icon 
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load(r"photos\enemy.png")
pygame.display.set_icon(icon)

# player image 
playerImg = pygame.image.load(r"photos\spaceship.png")
playerX = 370
playerY = 480
playerX_change = 0

# enemy image 
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
numOfEnemies = 6

for i in range(numOfEnemies):
    enemyImg.append(pygame.image.load(r"photos\enemy.png"))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(0.3)
    enemyY_change.append(40)

#bullet 
bullImg = pygame.image.load(r"photos\bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = .8
bullet_state = 'ready'  


score = 0


# Create the players 
# player function 
def player(x,y):
    screen.blit(playerImg,(x,y))

#  enemy function 
def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))

def fire_bullet(x,y):
    global bullet_state 
    bullet_state = 'fire'
    screen.blit(bullImg, (x + 16, y + 10))

def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY-bulletY, 2)))
 
    if distance  < 27:
        return True
    else:
        return False


# Game Loop 
running = True
while running:
    # This is the screen ----> RGB from 0 to 255 
    screen.fill((0,0,0))

    # This is the background 
    screen.blit(bg,(0,0))

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
        if event.key == pygame.K_UP:
            if bullet_state is 'ready':
                bulletX = playerX
                fire_bullet(playerX,bulletY)
            # print("space down")


    if event.type == pygame.KEYUP:
         if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
             playerX_change = 0
            #  print("keystoke has been released")


    # Player move on screen 
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736


    # Enemy move on screen 
    for i in range(numOfEnemies):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.3
            enemyY[i] += enemyY_change[i]
        #collision
       collision = isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
       if collision:
           bulletY = 480
           bullet_state = 'ready'
           score += 1
           print(score)
           enemyX[i] = random.randint(0,735)
           enemyY[i] = random.randint(50,150)

       enemy(enemyX[i],enemyY[i],i)

    if bulletY <=0 :
        bulletY = 480
        bullet_state = 'ready'
    # bullet movement 
    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change


    


    player(playerX,playerY)
    



    pygame.display.update()


# adding background 