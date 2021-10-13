import pygame

# first we need to make main surface
WIDTH, HEIGHT = 900,500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))

# game loop, infinite loop we will terminate when we 
# end the game
def main():

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        
        pygame.quit()