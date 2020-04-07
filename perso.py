class Perso:

    nbr_obj = 0
    inventory = []
    IS_ALIVE = True

    def __init__(self, type):
        if type == "guard":
            self.pos_x, self.pos_y = 7, 13
        if type == "gyver":
            self.pos_x, self.pos_y = 0, 1

    # MacGyver movement
    def moving(self, board, orientation):
        if orientation == "UP":
            if board.maze[self.pos_x - 1][self.pos_y] == '#':   # do nothing if the next square is a wall
                pass
            else:
                board.case_is_object(self, "up")    # call the add object function
                # inversion of MacGyver's box and its destination
                board.maze[self.pos_x - 1][self.pos_y] = '@'
                board.maze[self.pos_x][self.pos_y] = ' '
                self.pos_x -= 1     # update of MacGyver's positions

        elif orientation == "DOWN":
            if board.maze[self.pos_x + 1][self.pos_y] == '#':
                pass
            else:
                board.case_is_object(self, "down")
                board.maze[self.pos_x + 1][self.pos_y] = '@'
                board.maze[self.pos_x][self.pos_y] = ' '
                self.pos_x += 1

        elif orientation == "RIGHT":
            if board.maze[self.pos_x][self.pos_y + 1] == '#':
                pass
            else:
                board.case_is_object(self, "right")
                board.maze[self.pos_x][self.pos_y + 1] = '@'
                board.maze[self.pos_x][self.pos_y] = ' '
                self.pos_y += 1

        elif orientation == "LEFT":
            if board.maze[self.pos_x][self.pos_y - 1] == '#':
                pass
            else:
                board.case_is_object(self, "left")
                board.maze[self.pos_x][self.pos_y - 1] = '@'
                board.maze[self.pos_x][self.pos_y] = ' '
                self.pos_y -= 1
