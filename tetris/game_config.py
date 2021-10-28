# 20 * 10 square grid, each grid will have 30 pixels
import pygame
import numpy as np
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

class shape_list:
    def __init__(self):
        self.list = []
    def add_shape(self,shape):
        self.list.append(shape)
    
    def status_update():
        pass


class shape:
    def __init__(self,type):
        self.main = type # block type

    def okay_to_move(self,status,direction):
        # push button -> if it can move, move.
        # -> if not, either not move or stack
        for rect in self.main:
            pass # left cannot be done
        

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

    def grav(self, speed):
        for rect in self.main:
            rect.y += speed

    def handle_movements(key_pressed):
        
        pass
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



            


        
