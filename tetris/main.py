from numpy.core.defchararray import index
import game_config as g
import pygame
import numpy as np
import random

# first make a screen with the given width and height
# Let's make a movement that we drop the block to the bottom
# now let's try to make a block since it is a first time let's create a 4*1 block 10/12/2021

WIN = pygame.display.set_mode((g.WIDTH,g.HEIGHT))
pygame.display.set_caption("My First Game, Tetris")
block_img = pygame.image.load('IMG_1598.png')
block_img =  pygame.transform.scale(block_img, (g.grid_width,g.grid_height))

# before it moves, it needs to check
# 1) where the block is and see it can move into the direction that wants to go
# 2) when blocked it cannot move to left and right
# 2-1) if it touch the bottom, if there is a 1 right below the block it gets stuck 
# 3) downward velocity

def handle_movement(i, keys_pressed,shapes,status):
    if keys_pressed[pygame.K_LEFT] and shapes.x > 0: # left
        if status[shapes.y // g.grid_height][shapes.x // g.grid_width -1 ] != 1:
            shapes.x -= g.grid_width
    if keys_pressed[pygame.K_RIGHT] and shapes.x  + shapes.width < g.WIDTH: # Righ
        if status[shapes.y // g.grid_height][shapes.x // g.grid_width +1 ] != 1:
            shapes.x += g.grid_width
    
    if keys_pressed[pygame.K_DOWN] and shapes.list[i].bottom_y()  < g.HEIGHT: # Down
        # if it is in ground place on the ground
        # case 1, there is no block on the bottom
        shapes.list[i].coor_update("down")
        print(shapes.list[i].bottom_y() // g.grid_height)
        if shapes.list[i].bottom_y() // g.grid_height == 20:
            shapes,i= status_update(status, shapes,i)

    return shapes,i


def draw2(shapes):
    WIN.fill(g.WHITE)
    for shape in shapes.list:
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
    shape_list = g.shape_list()
    shape = g.shape(random.choice(g.BLOCKS))
    shape_list.add_shape(shape)
    
    run = True
    i = 0
    j = 0
    while run:
        j += 1
        clock.tick(g.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed()
        #shape_list.handle_movement(keys_pressed)
        shape_list,i = handle_movement(i,keys_pressed,shape_list,status)
        draw2(shape_list)

    pygame.quit()


if __name__ == "__main__":
    main()
