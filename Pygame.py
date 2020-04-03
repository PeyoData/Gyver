import pygame
from pygame.constants import *


class Pygame:
    def __init__(self):
        self.images = dict()

        pygame.init()
        # creation of the windows
        self.windows = pygame.display.set_mode((1100, 700))
        pygame.display.set_caption("MacGyver Escape")

        self.images["wall"] = pygame.image.load("img/wall.png").convert()
        self.images["perso"] = pygame.image.load("img/perso.png").convert()
        self.images["object"] = pygame.image.load("img/object.png").convert()
        self.images["guard"] = pygame.image.load("img/guard.png").convert()
        self.images["ground"] = pygame.image.load("img/ground.png").convert()

    def display(self, lab):

        x = 237
        y = 250
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

                x += 42
            x = 237
            y += 39
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

    def display_inventory(self, inventory):
        font = pygame.font.SysFont("Arial", 20)
        text = font.render("INVENTORY", 0, (255, 255, 255))
        self.windows.blit(text, (950, 20))
        x = 950
        y = 50
        self.windows.blit(self.images["wall"], (950, y))
        self.windows.blit(self.images["wall"], (1000, y))
        self.windows.blit(self.images["wall"], (1050, y))
        for item in inventory:
            self.windows.blit(self.images["object"], (x, y))
            x += 50

