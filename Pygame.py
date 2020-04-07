import pygame
from pygame.constants import *


class Pygame:
    def __init__(self):
        self.images = dict()

        pygame.init()
        self.windows = pygame.display.set_mode((1100, 700))     # creation of the windows
        pygame.display.set_caption("MacGyver Escape")

        self.images["#"] = pygame.image.load("img/wall.png").convert()
        self.images["@"] = pygame.image.load("img/perso.png").convert()
        self.images["E"] = pygame.image.load("img/object.png").convert()
        self.images["P"] = pygame.image.load("img/object2.png").convert()
        self.images["N"] = pygame.image.load("img/object3.png").convert()
        self.images["g"] = pygame.image.load("img/guard.png").convert()
        self.images[" "] = pygame.image.load("img/ground.png").convert()
        # self.images["final_win"] == pygame.image.load("img/win.png").convert()
        # self.images["final_lose"] == pygame.image.load("img/lose.png").convert()

    def display(self, lab):

        x = 237
        y = 250
        nbr = 0
        for line in lab:
            for case in line:
                self.windows.blit(self.images[case], (x, y))
                x += 42
            x = 237
            y += 39
        pygame.display.flip()

    def get_direction(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    return "UP"
                elif event.key == K_DOWN:
                    return "DOWN"
                elif event.key == K_RIGHT:
                    return "RIGHT"
                elif event.key == K_LEFT:
                    return "LEFT"

    def display_inventory(self, inventory):
        font = pygame.font.SysFont("Arial", 20)
        text = font.render("INVENTORY", 0, (255, 255, 255))
        self.windows.blit(text, (950, 20))
        x = 950
        y = 50
        self.windows.blit(self.images["#"], (950, y))
        self.windows.blit(self.images["#"], (1000, y))
        self.windows.blit(self.images["#"], (1050, y))
        for item in inventory:
            self.windows.blit(self.images[item], (x, y))
            x += 50

    def final_screen(self, inventory):
        if len(inventory) == 3:
            self.windows.blit(self.images["g"], (950, 30))
        else:
            self.windows.blit(self.images["N"], (950, 30))
        pygame.display.flip()
        pygame.time.delay(5000)

