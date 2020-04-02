import pygame
from pygame.constants import *


class Pygame:
    def __init__(self):
        self.images = dict()

        pygame.init()
        # creation of the windows
        self.windows = pygame.display.set_mode((640, 480), pygame.RESIZABLE)

        self.images["background"] = pygame.image.load("img/background.jpg").convert()
        self.images["wall"] = pygame.image.load("img/wall.png").convert()
        self.images["perso"] = pygame.image.load("img/perso.png").convert()
        self.images["object"] = pygame.image.load("img/object.png").convert()
        self.images["guard"] = pygame.image.load("img/guard.png").convert()
        self.images["ground"] = pygame.image.load("img/ground.png").convert()


    def display(self, lab):
        x = 0
        y = 0
        nbr = 0
        for line in lab:
            for case in line:
                if case == "#":
                    self.windows.blit(self.images["wall"], (x, y))
                elif case == "@":
                    self.windows.blit(self.images["perso"], (x, y))
                elif case == "°":
                    self.windows.blit(self.images["object"], (x, y))
                elif case == "g":
                    self.windows.blit(self.images["guard"], (x, y))
                elif case == " ":
                    self.windows.blit(self.images["ground"], (x, y))

                x += 22
            x = 0
            y += 19
        pygame.display.flip()

    def get_direction(self):
        for event in pygame.event.get():
            if event.type == QUIT:  # Si un de ces événements est de type QUIT
                pass
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    return "UP"
                elif event.key == K_DOWN:
                    return "DOWN"
                elif event.key == K_RIGHT:
                    return "RIGHT"
                elif event.key == K_LEFT:
                    return "LEFT"

    def display_inventor(self, inventory):
        for item in inventory:
            print(f"Inventory: ${''.join(item)}")
