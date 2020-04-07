import sys

import perso
import board
import CLI
import Pygame


class Main:
    gyver = perso.Perso("gyver")
    guard = perso.Perso("guard")
    main_board = board.Board(15, 8, gyver, guard)

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
            view.display(self.main_board.maze)
            view.display_inventory(self.gyver.inventory)

            action = view.get_direction()
            self.gyver.moving(self.main_board, action)

        # output of the while loop, MacGyver met the guard
        view.final_screen(self.gyver.inventory)


if __name__ == "__main__":  # Main is to start the play like a program
    Main()
