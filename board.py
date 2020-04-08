import random


class Board(object):
    """Pygame Class"""

    maze = []

    def __init__(self, width, height, gyver, guard):
        self.width = width
        self.height = height
        self.maze = self.maze_init(gyver, guard)
        self.dict_object = ('E', 'N', 'P')

    def maze_init(self, gyver, guard):
        """Initialize the maze from a .txt file"""
        brut_maze = []
        with open("waze.txt", "r") as openfile:
            for line in openfile.readlines():
                brut_maze.append(list(line))

        for element in brut_maze:
            if len(element) == 16:
                element.pop()

        brut_maze[gyver.pos_x][gyver.pos_y] = "@"
        brut_maze[guard.pos_x][guard.pos_y] = "g"
        temp_pos = self.init_objects(brut_maze)
        brut_maze[temp_pos[0]][temp_pos[1]] = "E"
        temp_pos = self.init_objects(brut_maze)
        brut_maze[temp_pos[0]][temp_pos[1]] = "N"
        temp_pos = self.init_objects(brut_maze)
        brut_maze[temp_pos[0]][temp_pos[1]] = "P"
        return brut_maze

    def init_objects(self, brut_maze):
        """Set objects random positions """
        pos_x = 0
        pos_y = 0
        while brut_maze[pos_x][pos_y] in ("#", "@", "g", "E", "P", "N"):
            pos_x = random.randint(1, self.height - 2)
            pos_y = random.randint(1, self.width - 2)

        return pos_x, pos_y

    def case_is_object(self, perso, orientation):
        """Object collect management"""
        if orientation == "up":
            if self.maze[perso.pos_x - 1][perso.pos_y] in ('E', 'N', 'P'):
                perso.inventory.append(self.maze[perso.pos_x - 1][perso.pos_y])

        elif orientation == "down":
            if self.maze[perso.pos_x + 1][perso.pos_y] in ('E', 'N', 'P'):
                perso.inventory.append(self.maze[perso.pos_x + 1][perso.pos_y])

        elif orientation == "right":
            if self.maze[perso.pos_x][perso.pos_y + 1] in ('E', 'N', 'P'):
                perso.inventory.append(self.maze[perso.pos_x][perso.pos_y + 1])

        elif orientation == "left":
            if self.maze[perso.pos_x][perso.pos_y - 1] in ('E', 'N', 'P'):
                perso.inventory.append(self.maze[perso.pos_x][perso.pos_y - 1])
