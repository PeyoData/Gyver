import os


class CLI:

    def __init__(self):
        pass

    def display(self, lab):
        os.system('clear')
        for list in lab:
            print("".join(list))

    def get_direction(self):
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

    def display_inventor(self, inventory):
        for item in inventory:
            print(f"Inventory: ${''.join(item)}")
