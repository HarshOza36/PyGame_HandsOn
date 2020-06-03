# Changing and making test1 better

import pygame

# setting Pygame
pygame.init()
winWidth = 750
winHeight = 550
window = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption('Fighter Madness v1')

# Character Variables
x = 50
y = 400
wid = 64
hgt = 64
vel = 10
isJump = False
jumpVal = 10
# Addition to test1
left = False
right = False
walkCount = 0

# Load Sprites

walkRight = [pygame.image.load('Sprites/R1.png'), pygame.image.load('Sprites/R2.png'), pygame.image.load('Sprites/R3.png'), pygame.image.load('Sprites/R4.png'), pygame.image.load(
    'Sprites/R5.png'), pygame.image.load('Sprites/R6.png'), pygame.image.load('Sprites/R7.png'), pygame.image.load('Sprites/R8.png'), pygame.image.load('Sprites/R9.png')]


walkLeft = [pygame.image.load('Sprites/L1.png'), pygame.image.load('Sprites/L2.png'), pygame.image.load('Sprites/L3.png'), pygame.image.load('Sprites/L4.png'), pygame.image.load(
    'Sprites/L5.png'), pygame.image.load('Sprites/L6.png'), pygame.image.load('Sprites/L7.png'), pygame.image.load('Sprites/L8.png'), pygame.image.load('Sprites/L9.png')]


bg = pygame.image.load('Sprites/bg.jpg')
char = pygame.image.load('Sprites/standing.png')


def reDraw():  # To redraw the game window
    global walkCount
    # We give background instead of just color
    window.blit(bg, (0, 0))
    # We had created rectangle as our character   in test1 lets replace that with sprite

    # 27 because we have total 9 sprites*3 frames to show=27 .
    if((walkCount+1) >= 27):
        walkCount = 0
    if(left):
        window.blit(walkLeft[walkCount//3], (x, y))
        walkCount += 1
    elif(right):
        window.blit(walkRight[walkCount//3], (x, y))
        walkCount += 1
    else:
        window.blit(char, (x, y))
        walkCount += 1

    pygame.display.update()


# Creating a loop variable
runGame = True


# Intialize Clock
clock = pygame.time.Clock()

# MainLoop-Infinite Loop
while runGame:
    # pygame.time.delay(150)  # Clock
    clock.tick(27)  # So this is our FPS

    # Accessing Pygame events for controlling the game
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            runGame = False

    # lets create movement controls
    keys = pygame.key.get_pressed()

    # Move -  Jump Left right
    # Jump controlling : user should not move up or down manually when used jump

    if(not isJump):
        # Stop up and down movement so deleted that from test1
        if(keys[pygame.K_SPACE]):
            isJump = True
            right = False
            left = False
            walkCount = 0
    # Jump code when Active
    else:
        if(jumpVal >= -10):
            negative = 1
            if(jumpVal < 0):
                negative = -1
            y -= ((jumpVal**2)/2)*(negative)
            jumpVal -= 1
        else:
            isJump = False
            jumpVal = 10

    # User can move left or right when jumping
    if(keys[pygame.K_LEFT] and x > vel):
        # Subtract X coordinate using velocity to move
        x -= vel
        left = True
        right = False
    elif(keys[pygame.K_RIGHT] and x < winWidth-wid):
        # Add X coordinate using velocity to move
        x += vel
        right = True
        left = False
    else:
        right = False
        left = False
        walkCount = 0

    reDraw()


pygame.quit()
