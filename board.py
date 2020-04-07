import random

class Board:

    maze = []

    def __init__(self, width, height, gyver, guard):
        self.width = width
        self.height = height
        self.maze = self.maze_init(gyver, guard)
        self.dict_object = ('E', 'N', 'P')

    def maze_init(self, gyver, guard):
        brut_maze = []
        with open("waze.txt", "r") as file:
            for line in file.readlines():
                brut_maze.append(list(line))

        for e in brut_maze:
            if len(e) == 16:
                e.pop()

        brut_maze[gyver.pos_x][gyver.pos_y] = "@"
        brut_maze[guard.pos_x][guard.pos_y] = "g"
        brut_maze[self.init_objects(brut_maze)[0]][self.init_objects(brut_maze)[1]] = "E"
        brut_maze[self.init_objects(brut_maze)[0]][self.init_objects(brut_maze)[1]] = "N"
        brut_maze[self.init_objects(brut_maze)[0]][self.init_objects(brut_maze)[1]] = "P"
        return brut_maze

    def init_objects(self, brut_maze):
        x = 0
        y = 0
        while brut_maze[x][y] != " ":
            x = random.randint(1, self.height - 2)
            y = random.randint(1, self.width - 2)
        return x, y

    def case_is_object(self, perso, orientation):

        if orientation == "up":
            if self.maze[perso.pos_x - 1][perso.pos_y] in ('E', 'N', 'P'):
                perso.inventory.append(self.maze[perso.pos_x - 1][perso.pos_y])

        elif orientation == "down":
            if self.maze[perso.pos_x + 1][perso.pos_y] in ('E', 'N', 'P'):
                perso.inventory.append(self.maze[perso.pos_x + 1][perso.pos_y])

        elif orientation == "right":
            if self.maze[perso.pos_x][perso.pos_y + 1] in ('E', 'N', 'P'):
                perso.inventory.append(self.maze[perso.pos_x][perso.pos_y + 1] )

        elif orientation == "left":
            if self.maze[perso.pos_x][perso.pos_y - 1] in ('E', 'N', 'P'):
                perso.inventory.append(self.maze[perso.pos_x][perso.pos_y - 1])

