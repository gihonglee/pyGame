import pygame
import os # we are going to use os

# first we need to make main surface
WIDTH, HEIGHT = 900,500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("First Game!") # change the name caption

WHITE = (255,255,255)
FPS = 60 # how many frame/sec to be updated
VEL = 5
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

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
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))  # draw a surface into the screen
    pygame.display.update() # pygame won't update unless we manually include this line of code


# game loop, infinite loop we will terminate when we 
# end the game
def main():

    red = pygame.Rect(700,300, SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100,300, SPACESHIP_WIDTH,SPACESHIP_HEIGHT)


    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS) # Control the speed of while loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        # wasd for the yellow / arrow key for the red
        
        keys_pressed = pygame.key.get_pressed()
        # sequence of boolean values representing the
        # state of every key on the keyboard.
        if keys_pressed[pygame.K_a]: #left
            yellow.x -= VEL
        if keys_pressed[pygame.K_d]: #left
            yellow.x += VEL
        if keys_pressed[pygame.K_w]: #left
            yellow.y -= VEL
        if keys_pressed[pygame.K_s]: #left
            yellow.y += VEL
        # i am having the trouble


        draw_window(red, yellow)
       
    pygame.quit()

if __name__ == "__main__":
    main() # if we do not put this main inside of this
            # main loop, whenever this file is called in other
            # location, it will pop up the screen