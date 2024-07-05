#In this file, i converted my DAY1 code into OOPS
import pygame
from pygame.locals import *
class game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("My Snake Game")
        self.surface = pygame.display.set_mode((1000, 500))
        self.surface.fill((112, 15, 63))
        self.block = pygame.image.load("snakehead.png").convert_alpha()  # Use convert_alpha() for transparency support
        self.block = pygame.transform.scale(self.block, (55, 25))  # Resize to 50x50 pixels
        self.x_co = 500  # Start in the middle of the screen
        self.y_co = 250  # Start in the middle of the screen
        self.surface.blit(self.block, (self.x_co,self.y_co))
        pygame.display.flip()
        self.running = True
        

    def drawblock(self):
        self.surface.fill((112, 15, 63))  # Clear the surface
        self.surface.blit(self.block, (self.x_co, self.y_co))  # Draw the block at new coordinates
        pygame.display.flip()  # Update the display
        pygame.time.delay(100)  # Delay for 100 milliseconds
        
        
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type==QUIT:
                    self.running=False
                elif event.type== KEYDOWN:
                    if event.key == K_DOWN:
                        self.y_co += 10
                    
                    elif event.key == K_UP:
                        self.y_co -= 10
                    
                    elif event.key == K_LEFT:
                        self.x_co -= 10
                    
                    elif event.key == K_RIGHT:
                        self.x_co += 10
                    self.drawblock()
        pygame.quit()



if __name__ == "__main__":
    snakegame= game()
    snakegame.run()

    