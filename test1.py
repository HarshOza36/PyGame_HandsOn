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
wid = 40
hgt = 60
vel = 10
isJump = False
jumpVal = 10


# Creating a loop variable

runGame = True
while runGame:
    pygame.time.delay(150)  # Clock

    # Accessing Pygame events for controlling the game
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            runGame = False

    # lets create movement controls
    keys = pygame.key.get_pressed()

    # Move UP Down Left right
    # Jump controlling : user should not move up or down manually when used jump

    if(not isJump):
        if(keys[pygame.K_UP] and y > vel):
            # Subtract Y coordinate using velocity to move
            y -= vel
        if(keys[pygame.K_DOWN] and y < winHeight-hgt):
            # Add Y coordinate using velocity to move
            y += vel
        if(keys[pygame.K_SPACE]):
            isJump = True
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
    if(keys[pygame.K_RIGHT] and x < winWidth-wid):
        # Add X coordinate using velocity to move
        x += vel

    # We fill the background so the character doesnt clone try removing this and seeing the output.

    window.fill((255, 255, 255))
    # Lets Create a rectangle
    # Syntax rect(window,(R,G,B),(X,Y,Width,Height))
    pygame.draw.rect(window, (255, 25, 0), (x, y, wid, hgt))

    # To add the rectangle(Thats our character this moments)
    pygame.display.update()
pygame.quit()
