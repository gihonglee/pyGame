# 20 * 10 square grid, each grid will have 30 pixels
import pygame
import numpy as np
import random
grid_width = 35
grid_height = 35
grid_num_x = 10
grid_num_y = 20
VEL = 35
FPS = 5
WIDTH = grid_width * (grid_num_x)
HEIGHT = grid_height * (grid_num_y)


# Color
WHITE = (255,255,255)

# what do i need to define?

i = [pygame.Rect(0,0, grid_width,grid_height),
    pygame.Rect(0, grid_width,  grid_width, grid_height),
    pygame.Rect(0, grid_width*2,  grid_width, grid_height),
    pygame.Rect(0, grid_width*3,  grid_width, grid_height)]

j = [pygame.Rect(0,0, grid_width,grid_height),
    pygame.Rect(0, grid_width,  grid_width, grid_height),
    pygame.Rect(grid_width, grid_width,  grid_width, grid_height),
    pygame.Rect(grid_width*2, grid_width,  grid_width, grid_height)]

l = [pygame.Rect(0,grid_width, grid_width,grid_height),
    pygame.Rect(grid_width, grid_width,  grid_width, grid_height),
    pygame.Rect(grid_width*2, grid_width,  grid_width, grid_height),
    pygame.Rect(grid_width*2, 0,  grid_width, grid_height)]

o = [pygame.Rect(0,0, grid_width,grid_height),
    pygame.Rect(0, grid_width,  grid_width, grid_height),
    pygame.Rect(grid_width, grid_width,  grid_width, grid_height),
    pygame.Rect(grid_width, 0,  grid_width, grid_height)]

s = [pygame.Rect(0,grid_width, grid_width,grid_height),
    pygame.Rect(grid_width, grid_width,  grid_width, grid_height),
    pygame.Rect(grid_width, 0,  grid_width, grid_height),
    pygame.Rect(grid_width*2, 0,  grid_width, grid_height)]

t = [pygame.Rect(0,grid_width, grid_width,grid_height),
    pygame.Rect(grid_width, grid_width,  grid_width, grid_height),
    pygame.Rect(grid_width*2, grid_width,  grid_width, grid_height),
    pygame.Rect(grid_width, 0,  grid_width, grid_height)]

z = [pygame.Rect(0,0, grid_width,grid_height),
    pygame.Rect(grid_width, grid_width,  grid_width, grid_height),
    pygame.Rect(grid_width*2, grid_width,  grid_width, grid_height),
    pygame.Rect(grid_width, 0,  grid_width, grid_height)]

BLOCKS = [i,j,l,o,s,t,z]


class shape:
    def __init__(self,type):
        self.main = type # block type

    def okay_to_move(self,status,direction):
        # push button -> if it can move, move.
        # -> if not, either not move or stack
        for rect in self.main:
            pass # left cannot be done

    def handle_movements(key_pressed):
        pass
        
    def get_coor(self):
        coor = np.zeros((4,2))
        i = 0
        j = 0
        for unit in self.main:
            coor[i][j] = unit.x
            coor[i][j+1] = unit.y
            i += 1
        return coor

    def handle_movement(self,shape_list,keys_pressed,status, drop = 0):
        drop = drop
        coor  = self.get_coor()
        left = 0
        right = 0
        down = 0
        rotate = 0
        for unit in self.main: 
            # check whether there is any block next to the direction where we are trying to go
            status[unit.y // grid_height][unit.x // grid_width -1 ] != 1
            left += 1
        for unit in self.main: 
            # check whether there is any block next to the direction where we are trying to go
            if unit.x // grid_width == 9:
                right =4
            else:
                status[unit.y // grid_height][unit.x // grid_width +1 ] != 1
                right += 1
        for unit in self.main: 
            # check whether there is any block next to the direction where we are trying to go
            if unit.y // grid_height == 19:
                down =4
            else:
                status[unit.y  // grid_height + 1][unit.x // grid_width] != 1
                down += 1

        if (keys_pressed[pygame.K_LEFT] and all(coor[:,0] > np.zeros((1,1)[0])) 
            and left == 4):
            for unit in self.main:
                unit.x -= grid_width

        if (keys_pressed[pygame.K_RIGHT] and all(coor[:,0] + grid_width < (np.ones((1,4)) * WIDTH)[0]) and right == 4): # Righ
            for unit in self.main:
                unit.x += grid_width
        
        if (keys_pressed[pygame.K_DOWN] or drop == 1) and all((coor[:,0] + grid_width)  < (np.ones((1,4)) * HEIGHT)[0]) and down == 4: # Down
            # if it is in ground place on the ground
            # case 1, there is no block on the bottom
            for unit in self.main:
                unit.y += grid_width

        # if they either touched the ground (one of the unit touch the ground) or one of the unit touched the 1 in status
        
        coor  = self.get_coor()
        s = 0
        if 19* grid_height in coor[:,1]:
            for unit in self.main:
                status[unit.y // grid_height][unit.x // grid_width] = 1
            shape_list.append(shape(random.choice(BLOCKS)))
        else:
            for unit in self.main:
                if (status[unit.y // grid_height + 1][unit.x // grid_width] == 1):
                    s = 1
            if s == 1:
                for unit in self.main:
                    status[unit.y // grid_height][unit.x // grid_width] = 1
                shape_list.append(shape(random.choice(BLOCKS)))


    def coor_update(self,direction):
        if direction == "left":     
            for rect in self.main:
                rect.x -= grid_height
        elif direction == "right":
            for rect in self.main:
                rect.x += grid_height
        elif direction == "down":
            for rect in self.main:
                rect.y += grid_height

    def rotate(self):
        pass

    def bottom_y(self):
        index = 0
        y = -1
        for rect in self.main:
            if rect.y > y:
                y = rect.y
            index += 1
        return y + grid_height


a = shape(i)
coor = a.get_coor()

#print(coor)
print(coor[:,0] + grid_width)
print((np.ones((1,4)) * HEIGHT)[0])
print(all((coor[:,0] + grid_width)  < (np.ones((1,4)) * HEIGHT)[0]))

         
