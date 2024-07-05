import pygame
from pygame.locals import *


def drawblock(surface, block, x_co, y_co):
    surface.fill((112, 15, 63))  # Clear the surface
    surface.blit(block, (x_co, y_co))  # Draw the block at new coordinates
    pygame.display.flip()  # Update the display
    pygame.time.delay(100)  # Delay for 100 milliseconds

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("My Snake Game")
    surface = pygame.display.set_mode((1000, 500))
    surface.fill((112, 15, 63))
    block = pygame.image.load("snakehead.png").convert_alpha()  # Use convert_alpha() for transparency support
    
    # Resize the block image to desired size
    block = pygame.transform.scale(block, (55, 25))  # Resize to 50x50 pixels
    
    x_co = 500  # Start in the middle of the screen
    y_co = 250  # Start in the middle of the screen
    surface.blit(block, (x_co, y_co))
    pygame.display.flip()
    
    cond = True
    while cond:
        for event in pygame.event.get():
            if event.type == QUIT:
                cond = False
            elif event.type == KEYDOWN:
                if event.key == K_DOWN:
                    y_co += 10
                    
                elif event.key == K_UP:
                    y_co -= 10
                    
                elif event.key == K_LEFT:
                    x_co -= 10
                    
                elif event.key == K_RIGHT:
                    x_co += 10

                drawblock(surface, block, x_co, y_co)
    
    pygame.quit()
