from numpy.core.defchararray import index
import game_config as g
import pygame
import os
import numpy as np

# first make a screen with the given width and height
# Let's make a movement that we drop the block to the bottom


WIN = pygame.display.set_mode((g.WIDTH,g.HEIGHT))
pygame.display.set_caption("My First Game, Tetris")
block = pygame.image.load('IMG_1598.png')
block =  pygame.transform.scale(block, (g.grid_width,g.grid_height))

# before it moves, it needs to check
# 1) where the block is and see it can move into the direction that wants to go
# 2) when blocked it cannot move to left and right
# 2-1) if it touch the bottom, if there is a 1 right below the block it gets stuck 
# 3) downward velocity

def handle_movement(i, keys_pressed,dummy_list,dummy_r,status,status2):
    if keys_pressed[pygame.K_LEFT] and dummy_r.x > 0: # left
        if status[dummy_r.y // g.grid_height][dummy_r.x // g.grid_width -1 ] != 1:
            dummy_r.x -= g.grid_width
    if keys_pressed[pygame.K_RIGHT] and dummy_r.x  + dummy_r.width < g.WIDTH: # Righ
        if status[dummy_r.y // g.grid_height][dummy_r.x // g.grid_width +1 ] != 1:
            dummy_r.x += g.grid_width
    if keys_pressed[pygame.K_DOWN] and dummy_r.y + dummy_r.height  < g.HEIGHT: # Down
        # if it is in ground place on the ground
        if dummy_r.y // g.grid_height:
            dummy_r.y += g.grid_width
        # case 1, there is no block on the bottom
        if (dummy_r.y // g.grid_height) == 19:
            status_update(status, status2, dummy_r,i)
        if (dummy_r.y // g.grid_height) < 19 and status[dummy_r.y // g.grid_height + 1][dummy_r.x // g.grid_width] == 1:
            status_update(status, status2, dummy_r,i)

        # case 2, there is some block on the bottom
    if status[dummy_r.y // g.grid_height][dummy_r.x // g.grid_width] == 1:
        dummy_list.append(pygame.Rect(0,0, g.grid_width,g.grid_height))
        i = i + 1
    return i


def draw(dummy_list):
    WIN.fill(g.WHITE)
    for dummy in dummy_list:
        WIN.blit(block, (dummy.x, dummy.y))
    pygame.display.update()

def status_update(status, status2, dummy,i):
    status[(dummy.y) // g.grid_height][dummy.x // g.grid_width] = 1
    status2[(dummy.y) // g.grid_height][dummy.x // g.grid_width] = i



def main():
    clock = pygame.time.Clock()
    status = np.zeros((g.grid_num_y,g.grid_num_x))
    status2 = np.zeros((g.grid_num_y,g.grid_num_x))
    dummy_list = [pygame.Rect(0,0, g.grid_width,g.grid_height)]
    run = True
    i = 0
    j = 0
    while run:
        j += 1
        clock.tick(g.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if j % g.FPS ==0:
            dummy_list[i].y += g.VEL
            print(dummy_list[i].y // g.VEL)
        if (dummy_list[i].y // g.grid_height) == 19:
            status_update(status, status2, dummy_list[i],i)
        if (dummy_list[i].y // g.grid_height) < 19 and status[dummy_list[i].y // g.grid_height + 1][dummy_list[i].x // g.grid_width] == 1:
            status_update(status, status2, dummy_list[i],i)
        if status[dummy_list[i].y // g.grid_height][dummy_list[i].x // g.grid_width] == 1:
            dummy_list.append(pygame.Rect(0,0, g.grid_width,g.grid_height))
            i = i + 1
            print("yes")
        keys_pressed = pygame.key.get_pressed()
        i = handle_movement(i,keys_pressed,dummy_list,dummy_list[i],status,status2)
        for i in range(g.grid_num_y-1, -1, -1):
            if sum(status[i,:]) == g.grid_num_x:
                print("time to delete mofos")
        draw(dummy_list)

    pygame.quit()

if __name__ == "__main__":
    main()
