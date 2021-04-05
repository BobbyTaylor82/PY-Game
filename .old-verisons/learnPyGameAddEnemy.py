import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))

playerImg = pygame.image.load(r"../photos/spaceship.png")
playerX = 360
playerY = 500
playerXChange = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


enemyImg = pygame.image.load(r"../photos/enemy.png")
enemyX = random.randint(32, 738)
enemyY = random.randint(50, 150)
enemyXChange = .2
enemyYChange = .2


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


enemy2Img = []
enemy2X = []
enemy2Y = []
enemy2YChange = []
def enemy2(x, y):
    screen.blit(enemy2Img, (x, y))

for i in range(0,8):
    enemy2Img.append(pygame.image.load(r"../photos/enemy2.png"))
    enemy2X.append(random.randint(32, 738))
    enemy2Y.append(-2)
    enemy2YChange.append(.2)


def enemy2(x, y):
    screen.blit(enemy2Img[i], (x, y))


bulletImg = pygame.image.load(r"../photos/bullet.png")
bulletX = 360
bulletY = 500
bulletXChange = 0
bulletState = 'ready'


def fireBullet(x, y):
    global bulletState
    bulletState = 'fire'
    screen.blit(bulletImg, (x, y))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# Game Loop
running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerXChange = -.4
        if event.key == pygame.K_RIGHT:
            playerXChange = .4
        if event.key == pygame.K_TAB:
            if bulletState is 'ready':
                fireBullet(playerX, playerY)
                bulletX = playerX
            print('enter')

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
            playerXChange = 0
        if event.key == pygame.K_RIGHT:
            playerXChange = 0

    playerX += playerXChange
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    player(playerX, playerY)

    # enemy movement
    enemyX += enemyXChange
    if enemyX <= 0:
        enemyXChange += .3
        enemyY += 40
        enemyX += enemyXChange
    elif enemyX >= 736:
        enemyXChange += -.3
        enemyY += 40
        enemyX += enemyXChange
    enemy(enemyX, enemyY)

    # enemy2 movement
    for i in range(0, 8):
        enemy2Y[i] += .2
        enemy2(enemy2X[i], enemy2Y[i])

        if enemy2Y[i] >= 620:
            enemy2Y[i] = -2
            enemy2X[i] = random.randint(32,738)


    if bulletY <= 0:
        bulletY = 480
        bulletState = 'ready'

    if bulletState is 'fire':
        bulletY -= 1
        fireBullet(bulletX, bulletY)

    print(enemyX, enemyY, bulletX, bulletY)
    collision = isCollision(enemyX, enemyY, bulletX, bulletY)

    if collision:
        bulletY = 480
        bulletState = 'ready'

        enemyX = random.randint(0, 735)
        enemyY = random.randint(50, 150)

    pygame.display.update()
