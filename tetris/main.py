import game_config as g
import pygame
import os

# first make a screen with the given width and height


WIN = pygame.display.set_mode((g.WIDTH,g.HEIGHT))
pygame.display.set_caption("My First Game, Tetris")

block = pygame.image.load('spaceship_red.png')
    
block =  pygame.transform.scale(block, (g.grid_width,g.grid_height))

def handle_movement(keys_pressed,dummy_r):
    if keys_pressed[pygame.K_LEFT] and dummy_r.x > 0: # left
        dummy_r.x -= g.grid_width
    if keys_pressed[pygame.K_RIGHT] and dummy_r.x  + dummy_r.width < g.WIDTH: # Right
        dummy_r.x += g.grid_width
    if keys_pressed[pygame.K_UP] and dummy_r.y> 0: # Up
        dummy_r.y -= g.grid_width
    if keys_pressed[pygame.K_a] and dummy_r.y + dummy_r.height  < g.HEIGHT: # Down
        dummy_r.y += g.grid_width
    print(dummy_r.x)
    print(dummy_r.y)
def draw(dummy_r):
    WIN.fill(g.WHITE)
    WIN.blit(block, (dummy_r.x, dummy_r.y))
    pygame.display.update()

def main():

    dummy_r = pygame.Rect(0,300, g.grid_num_x,g.grid_num_y)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw(dummy_r)
    

    keys_pressed = pygame.key.get_pressed()
    handle_movement(keys_pressed,dummy_r)
    dummy_r.y = dummy_r.y + 300
    draw(dummy_r)
    pygame.quit()

if __name__ == "__main__":
    main()