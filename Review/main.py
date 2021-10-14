import pygame
import os # we are going to use os

### Instantiate Constants
WIDTH, HEIGHT = 900,500 # Initialize the widht and width
WHITE = (255,255,255)
BLACK = (0,0,0)
FPS = 60 # how many frame/sec to be updated
VEL = 5
BULLET_VEL = 7
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
BORDER = pygame.Rect(WIDTH/2-5,0,10,HEIGHT)

WIN = pygame.display.set_mode((WIDTH,HEIGHT)) # set the width and height of the game
pygame.display.set_caption("First Game!") # change the name caption

YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets','spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets','spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)), 270)


def draw_window(red, yellow):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))  # draw a surface into the screen
    pygame.display.update() # pygame won't update unless we manually include this line of code

def yellow_handle_movement(keys_pressed,yellow):
    if keys_pressed[pygame.K_a] and yellow.x -VEL > 0: # left
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x  : # Right
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL>0: # Up
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 15: # Down
        yellow.y += VEL

def red_handle_movement(keys_pressed,red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x +BORDER.width: # left
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH: # Right
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL> 0: # Up
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y +VEL + red.height + 15 < HEIGHT: # Down
        red.y += VEL

# game loop, infinite loop we will terminate when we 
# end the game
def main():

    red = pygame.Rect(700,300, SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100,300, SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    bullets = []
    # Instantiate the rectangle object on the pygame (location and shape)
    # Assign the image of the blit object to be the location of the red and yellow object

    clock = pygame.time.Clock() # Control the speed of while loop
    run = True
    while run:
        clock.tick(FPS) # Control the speed of while loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if # this is to ensure that the key is not being press down for the bullet shooting

            
        # wasd for the yellow / arrow key for the red
        
        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed,yellow)
        red_handle_movement(keys_pressed, red)
        draw_window(red, yellow)
       
    pygame.quit()

if __name__ == "__main__":
    main() # if we do not put this main inside of this
            # main loop, whenever this file is called in other
            # location, it will pop up the screen