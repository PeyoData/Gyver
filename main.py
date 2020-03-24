import perso
import board
import case
import os

board = board.Board(15,8)
board.initialize()
# board.anoucement()
perso = perso.Perso()

#joue tant que 1
on_game = 1
while on_game:
    # os.system('clear')
    board.showing_board()
    action = input("")
    for i in (board.get_listCase()):
        if action == "z":
            if i.case_content == "perso":
                i.longitude -= 1
        elif action == "s":
            if i.case_content == "perso":
                i.longitude += 1
        elif action == "d":
            if i.case_content == "perso":
                i.latitude += 1
        elif action == "q":
            if i.case_content == "perso":
                i.latitude -= 1
        else:
            on_game = 0