from numpy.core.defchararray import index
import game_config as g
import pygame
import numpy as np
import random

# first make a screen with the given width and height
# Let's make a movement that we drop the block to the bottom
# now let's try to make a block since it is a first time let's create a 4*1 block 10/22/2021

WIN = pygame.display.set_mode((g.WIDTH,g.HEIGHT))
pygame.display.set_caption("My First Game, Tetris")
block_img = pygame.image.load('IMG_1598.png')
block_img =  pygame.transform.scale(block_img, (g.grid_width,g.grid_height))

# before it moves, it needs to check
# 1) where the block is and see it can move into the direction that wants to go
# 2) when blocked it cannot move to left and right
# 2-1) if it touch the bottom, if there is a 1 right below the block it gets stuck 
# 3) downward velocity

def draw2(shape_list):
    WIN.fill(g.WHITE)
    for shape in shape_list:
        for unit in shape.main:
            WIN.blit(block_img, (unit.x, unit.y))
    pygame.display.update()

def status_update(status, blocks,i):
    for block in blocks[i].main:
        status[(block.y) // g.grid_height][block.x // g.grid_width] = 1
    blocks.append(g.shape())
    i = i + 1
    return blocks,i

# let me define, shapes -> shape -> unit

def main():
    clock = pygame.time.Clock()
    status = np.zeros((g.grid_num_y,g.grid_num_x))
    shape = g.shape(random.choice(g.BLOCKS))
    shape_list= [shape]
    run = True
    i = 0
    j = 0
    while run:
        j += 1
        clock.tick(g.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if j % g.FPS == 0:        
            shape_list[-1].handle_movement(shape_list,keys_pressed,status,1)
        keys_pressed = pygame.key.get_pressed()
        shape_list[-1].handle_movement(shape_list,keys_pressed,status)
        draw2(shape_list)

    pygame.quit()


if __name__ == "__main__":
    main()
