from numpy.core.defchararray import index
import game_config as g
import pygame
import os
import numpy as np

# first make a screen with the given width and height
# Let's make a movement that we drop the block to the bottom


WIN = pygame.display.set_mode((g.WIDTH,g.HEIGHT))
pygame.display.set_caption("My First Game, Tetris")

block = pygame.image.load('spaceship_red.png')
    
block =  pygame.transform.scale(block, (g.grid_width,g.grid_height))

def handle_movement(keys_pressed,dummy_r,status):
    if keys_pressed[pygame.K_LEFT] and dummy_r.x > 0: # left
        dummy_r.x -= g.grid_width
    if keys_pressed[pygame.K_RIGHT] and dummy_r.x  + dummy_r.width < g.WIDTH: # Right
        dummy_r.x += g.grid_width
    if keys_pressed[pygame.K_UP] and dummy_r.y> 0: # Up
        dummy_r.y -= g.grid_width
    if keys_pressed[pygame.K_DOWN] and dummy_r.y + dummy_r.height  < g.HEIGHT: # Down
        dummy_r.y += g.grid_width
    if keys_pressed[pygame.K_z]: # Drop
        a = status[: , dummy_r.x // g.grid_width]
        print(a)
        j = 0
        for i in a:
            if i == 1:
                break
            else:
                j = j+1
        print(j)
        dummy_r.y = (j - 1) * dummy_r.height
    
def draw(dummy_list):
    WIN.fill(g.WHITE)
    for dummy in dummy_list:
        WIN.blit(block, (dummy.x, dummy.y))
    pygame.display.update()

def status_update(status, dummy):
    status[(dummy.y) // g.grid_width][dummy.x // g.grid_height] = 1


def main():
    clock = pygame.time.Clock()
    status = np.zeros((g.grid_num_y,g.grid_num_x))
    dummy_list = [pygame.Rect(0,0, g.grid_width,g.grid_height)]

    # dummy_r = pygame.Rect(0,0, g.grid_width,g.grid_height)
    # dummy_y = pygame.Rect(0,0, g.grid_width,g.grid_height)
    i = 0
    run = True
    while run:
        clock.tick(g.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    
        keys_pressed = pygame.key.get_pressed()
        handle_movement(keys_pressed,dummy_list[i],status)
        draw(dummy_list)
        if keys_pressed[pygame.K_z]:
            status_update(status,dummy_list[i])
            dummy_list.append(pygame.Rect(0,0, g.grid_width,g.grid_height))
            i = i + 1
        

    pygame.quit()

if __name__ == "__main__":
    main()