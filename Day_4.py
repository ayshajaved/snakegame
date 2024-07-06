import pygame
from pygame.locals import *
import time
import random

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("My Snake Game")
        self.surface = pygame.display.set_mode((1000, 500))
        self.surface.fill((112, 15, 63))
        self.block = pygame.image.load("block.jpg").convert_alpha()
        # self.block = pygame.transform.scale(self.block, (40, 40))
        self.food = pygame.image.load("apple.jpg").convert_alpha()
        # self.food = pygame.transform.scale(self.food, (40, 40))
        self.length = 1
        self.x_co = [500]  # List to store x coordinates of snake segments
        self.y_co = [250]  # List to store y coordinates of snake segments
        self.foodx = random.randint(0, 960)  # Adjusted to keep food within screen bounds
        self.foody = random.randint(0, 460)  # Adjusted to keep food within screen bounds
        self.surface.blit(self.food, (self.foodx, self.foody))
        self.surface.blit(self.block, (self.x_co[0], self.y_co[0]))
        pygame.display.flip()
        self.running = True
        self.direction = "right"

    def drawblock(self):
        self.surface.fill((112, 15, 63))
        self.surface.blit(self.food, (self.foodx, self.foody))
        for i in range(self.length):
            self.surface.blit(self.block, (self.x_co[i], self.y_co[i]))
        pygame.display.flip()
        pygame.time.delay(100)

    def move(self):
        for i in range(self.length - 1, 0, -1):
            self.x_co[i] = self.x_co[i - 1]
            self.y_co[i] = self.y_co[i - 1]
        if self.direction == "right":
            self.x_co[0] += 40
        elif self.direction == "left":
            self.x_co[0] -= 40
        elif self.direction == "up":
            self.y_co[0] -= 40
        elif self.direction == "down":
            self.y_co[0] += 40
        self.check_collision()
        self.drawblock()
    def display_game_over(self):
        font = pygame.font.SysFont("roman", 50)
        game_over_text = font.render("Game Over!", True, (255, 255, 255))
        self.surface.blit(game_over_text, (400, 250))
        pygame.display.flip()
        time.sleep(2)

    def check_collision(self):
        # Collision with the apple
        if abs(self.x_co[0] - self.foodx) < 40 and abs(self.y_co[0] - self.foody) < 40:
            self.length += 1
            self.x_co.append(self.x_co[-1])
            self.y_co.append(self.y_co[-1])
            self.foodx = random.randint(0, 960)
            self.foody = random.randint(0, 460)
    def collision(self):
        for i in range (self.length):
            if self.x_co[0] == self.x_co[i] and self.y_co[0] == self.y_co[i]:
                self.running = False
                self.display_game_over()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                elif event.type == KEYDOWN:
                    if event.key == K_DOWN and self.direction != "up":
                        self.direction = "down"
                    elif event.key == K_UP and self.direction != "down":
                        self.direction = "up"
                    elif event.key == K_LEFT and self.direction != "right":
                        self.direction = "left"
                    elif event.key == K_RIGHT and self.direction != "left":
                        self.direction = "right"
            self.move()
            time.sleep(0.01)
        pygame.quit()

if __name__ == "__main__":
    snakegame = Game()
    snakegame.run()
