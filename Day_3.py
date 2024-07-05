#in this program, i will mold by programm in a way that the block will move on its on and i will just change the direction of the block(snake) on pressing the keys
#In this file, i converted my DAY1 code into OOPS
import pygame
from pygame.locals import *
import time
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
        self.direction = "right"

    def drawblock(self):
        self.surface.fill((112, 15, 63))  # Clear the surface
        self.surface.blit(self.block, (self.x_co, self.y_co))  # Draw the block at new coordinates
        pygame.display.flip()  # Update the display
        pygame.time.delay(100)  # Delay for 100 milliseconds
        
    def move(self):
        if self.direction == "right":
            self.x_co+=10
        elif self.direction == "left":
            self.x_co-=10
        elif self.direction == "up":
            self.y_co-=10
        elif self.direction == "down":
            self.y_co+=10
        self.drawblock()




    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type==QUIT:
                    self.running=False
                elif event.type== KEYDOWN:
                    if event.key == K_DOWN:
                        self.direction= "down"
                    
                    elif event.key == K_UP:
                        self.direction="up"
                    
                    elif event.key == K_LEFT:
                        self.direction= "left"
                    
                    elif event.key == K_RIGHT:
                        self.direction="right"
                    self.drawblock()
            self.move()
            time.sleep(0.001)
        pygame.quit()



if __name__ == "__main__":
    snakegame= game()
    snakegame.run()

    