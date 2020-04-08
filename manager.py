import sys

import perso
import board
import cli
import Pygame


class Main:
    """Main class"""

    gyver = perso.Perso("gyver")
    guard = perso.Perso("guard")
    main_board = board.Board(15, 8, gyver, guard)

    def __init__(self):
        view = None
        if len(sys.argv) > 1:
            if sys.argv[1] == "-g":     # load graphic mode
                view = Pygame.Pygame()
            else:
                print("unknown argument")
                exit()
        else:
            view = cli.CLI()    # load CLI mode
        if view is not None:
            self.start(view)

    # as long as MacGyver's not on the same square as the guard...
    def start(self, view):
        """Game body"""
        while (self.gyver.pos_x, self.gyver.pos_y) != (self.guard.pos_x, self.guard.pos_y):
            view.display(self.main_board.maze)
            view.display_inventory(self.gyver.inventory)

            action = view.get_direction()
            self.gyver.moving(self.main_board, action)

        view.final_screen(self.gyver.inventory)     # loop output when MacGyver met the guard


if __name__ == "__main__":
    Main()
