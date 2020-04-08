import os


class CLI:

    def __init__(self):
        pass

    @staticmethod
    def display(lab):
        """Display the game"""

        os.system('clear')
        for list in lab:
            print("".join(list))

    @staticmethod
    def get_direction():
        """Receive Input"""

        key_input = input("")
        if key_input == "z":
            return "UP"
        elif key_input == "s":
            return "DOWN"
        elif key_input == "d":
            return "RIGHT"
        elif key_input == "q":
            return "LEFT"
        else:
            pass

    @staticmethod
    def display_inventory(inventory):
        """Show MacGyver inventory"""

        print("Inventory : ", end=" ")
        for item in inventory:
            print(item, end=" / ")
        print(" ")

    @staticmethod
    def final_screen(inventory):
        """Display the Victory/Lose panel"""

        if len(inventory) == 3:
            print("YOU SUCCEED !")
        else:
            print("YOU LOOSE...")

