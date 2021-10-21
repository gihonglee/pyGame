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

def handle_movement(keys_pressed,dummy_r):
    if keys_pressed[pygame.K_LEFT] and dummy_r.x > 0: # left
        dummy_r.x -= g.grid_width
    if keys_pressed[pygame.K_RIGHT] and dummy_r.x  + dummy_r.width < g.WIDTH: # Right
        dummy_r.x += g.grid_width
    if keys_pressed[pygame.K_UP] and dummy_r.y> 0: # Up
        dummy_r.y -= g.grid_width
    if keys_pressed[pygame.K_DOWN] and dummy_r.y + dummy_r.height  < g.HEIGHT: # Down
        dummy_r.y += g.grid_width
    if keys_pressed[pygame.K_z]: # Drop
        dummy_r.y = g.HEIGHT - dummy_r.height
    
def draw(dummy_list):
    WIN.fill(g.WHITE)
    for dummy in dummy_list:
        WIN.blit(block, (dummy.x, dummy.y))
    pygame.display.update()

def status(x,y,type):
    pass


def main():
    clock = pygame.time.Clock()
    dummy_list = []
    dummy = pygame.Rect(0,0, g.grid_width,g.grid_height)
    dummy_list.append(dummy)
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
        handle_movement(keys_pressed,dummy_list[i])
        draw(dummy_list)
        if keys_pressed[pygame.K_z]:
            dummy_list.append(pygame.Rect(0,0, g.grid_width,g.grid_height))
            i = i + 1

    pygame.quit()

if __name__ == "__main__":
    main()