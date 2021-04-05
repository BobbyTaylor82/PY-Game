import pygame
import math

# Initalize the pygame 
pygame.init()
# background
bg = pygame.image.load(r"photos/city-top-view.png")
pygame.mixer.init()
pygame.mixer.music.load(r'BLJR - Thursday Night EP - 02 BLJR - Thursday Night 2.wav')
pygame.mixer.music.play(-1)

# create the screen
# 800 W and 600 h 
# left to right 0 --> w
# top to bottom 0 --> h
screen = pygame.display.set_mode((1200, 600))

# caption and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load(r"photos/galaga.png")
pygame.display.set_icon(icon)

# player1 image
player1Img = pygame.image.load(r"photos/spaceship1.png")
player1X = 0
player1Y = 300
player1Ychange = 0


def player1(x, y):
    screen.blit(player1Img, (x, y))


# Player1 bullet
bullImg1 = pygame.image.load(r"photos\bullet.png")
bulletX1 = 0
bulletY1 = 480
bulletX_change1 = 30
bullet_state1 = 'ready'


def fire_bullet1(x, y):
    global bullet_state1
    bullet_state1 = 'fire'
    screen.blit(bullImg1, (x, y))


# player 1 hits player 2 (collision)
def isCollision1(player2X, player2Y, bulletX1, bulletY1):
    distance1 = math.sqrt((math.pow(player2X - bulletX1, 2)) + (math.pow(player2Y - bulletY1, 2)))

    if distance1 < 30:
        return True
    else:
        return False

# Score
scoreValue1 = 0
font1 = pygame.font.Font('freesansbold.ttf', 32)
textX1 = 10
textY1 = 10
def showScore1(x, y):
    score1 = font1.render("Score:" + str(scoreValue1), True, (255, 255, 255))
    screen.blit(score1, (x, y))

# ************************************************************

# player 2 image
player2Img = pygame.image.load(r"photos/spaceship2.png")
player2X = 1132
player2Y = 300
player2Ychange = 0
def player2(x, y):
    screen.blit(player2Img, (x, y))


# Player2 bullet
bullImg2 = pygame.image.load(r"photos\bullet.png")
bulletX2 = 1132
bulletY2 = 300
bulletX_change2 = 30
bullet_state2 = 'ready'
def fire_bullet2(x, y):
    global bullet_state2
    bullet_state2 = 'fire'
    screen.blit(bullImg2, (x, y))


def isCollision2(player1X, player1Y, bulletX2, bulletY2):
    distance1 = math.sqrt((math.pow(player1X - bulletX2, 2)) + (math.pow(player1Y - bulletY2, 2)))

    if distance1 < 30:
        return True
    else:
        return False


# Score
scoreValue2 = 0
font2 = pygame.font.Font('freesansbold.ttf', 32)
textX2 = 1080
textY2 = 10


def showScore2(x, y):
    score2 = font2.render("Score:" + str(scoreValue2), True, (255, 255, 255))
    screen.blit(score2, (x, y))


# Game Loop
running = True
while running:

    screen.fill((0, 0, 0))
    # This is the background
    screen.blit(bg, (0, 0))

    # quit game 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # KEYDOWN
    if event.type == pygame.KEYDOWN:
        # player 1
        if event.key == pygame.K_TAB:
            player1Ychange += -.1
            print("tab works")
        if event.key == pygame.K_LSHIFT:
            player1Ychange += .1
            print("L shift works")
        if event.key == pygame.K_LALT:
            if bullet_state1 is 'ready':
                bulletY1 = player1Y
                fire_bullet1(bulletX1, bulletY1)

        # player 2
        if event.key == pygame.K_UP:
            player2Ychange += -.1
        if event.key == pygame.K_DOWN:
            player2Ychange += .1
        if event.key == pygame.K_LEFT:
            if bullet_state2 is 'ready':
                bulletY2 = player2Y
                fire_bullet2(bulletX2, bulletY2)

    # ****************************************************************
    # KEYUP
    if event.type == pygame.KEYUP:
        # player 1
        if event.key == pygame.K_TAB:
            player1Ychange = 0
        if event.key == pygame.K_LSHIFT:
            player1Ychange = 0

        # player 2
        if event.key == pygame.K_UP:
            player2Ychange = 0

        if event.key == pygame.K_DOWN:
            player2Ychange = 0
    # ****************************************************************
    # Player Movement
    # Player 1
    player1Y += player1Ychange
    if player1Y <= 5:
        player1Y = 5
    elif player1Y >= 532:
        player1Y = 532
    # Player 2
    player2Y += player2Ychange
    if player2Y <= 5:
        player2Y = 5
    elif player2Y >= 532:
        player2Y = 532

    ##****************************************************************
    # Fire bullets
    # Player 1
    if bulletX1 >= 1200:
        bulletX1 = 0
        bullet_state1 = 'ready'
    if bullet_state1 is 'fire':
        bulletX1 += bulletX_change1
        fire_bullet1(bulletX1, bulletY1)

    # Player 2
    if bulletX2 <= 0:
        bulletX2 = 1132
        bullet_state2 = 'ready'
    if bullet_state2 is 'fire':
        bulletX2 -= bulletX_change2
        fire_bullet2(bulletX2, bulletY2)

    # *************************************************************
    # Collision
    # Player1 hits player 2
    collision1 = isCollision1(player2X, player2Y, bulletX1, bulletY1)
    if collision1:
        bulletX1 = 0
        bullet_state1 = 'ready'
        scoreValue1 += 1
        print(scoreValue1)
        player2X = 1132
        player2Y = 300
    # Player2 hits player 1
    collision2 = isCollision2(player1X, player1Y, bulletX2, bulletY2)
    if collision2:
        bulletX2 = 1132
        bullet_state2 = 'ready'
        scoreValue2 += 1
        print(scoreValue2)
        player1X = 0
        player1Y = 300

    player1(player1X, player1Y)
    player2(player2X, player2Y)

    showScore1(textX1, textY1)
    showScore2(textX2, textY2)

    pygame.display.update()
