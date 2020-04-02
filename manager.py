import sys

import perso
import board
import CLI
import Pygame


class Main:
    gyver = perso.Perso("gyver")
    guard = perso.Perso("guard")
    board = board.Board(15, 8, gyver, guard)

    def __init__(self):
        view = None
        if len(sys.argv) > 1:
            if sys.argv[1] == "-g":
                view = Pygame.Pygame()
            else:
                print("unknown argument")
                exit()
        else:
            view = CLI.CLI()
        if view is not None:
            self.start(view)

    # as long as MacGyver's not on the same square as the guard...
    def start(self, view):
        while (self.gyver.pos_x, self.gyver.pos_y) != (self.guard.pos_x, self.guard.pos_y):
            view.display(self.board.maze)
            # view.display_inventory(None)
            # board display
            action = view.get_direction()
            self.gyver.moving(self.board, action)

        # output of the while loop, MacGyver met the guard

        if self.gyver.nbr_obj == 3:
            print("YOU SUCCEED !")
        else:
            print("YOU LOOSE...")


if __name__ == "__main__":  # Main is to start the play like a program
    Main()
