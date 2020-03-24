import case

class Board:

    list_case = []
    #organisation de la grille
    construction = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                    1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 3, 1,
                    1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1,
                    1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1,
                    1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1,
                    1, 3, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1,
                    1, 0, 0, 0, 0, 0, 1, 1, 1, 3, 0, 1, 1, 4, 1,
                    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                    ]

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.list_case = self.initialize()

    # liste des elements(positions + contenu) en partant de la construction
    def initialize(self):
        list_case = []
        x = 0
        y = 0
        for e in range(len(self.construction)):
            if y == self.width:
                x +=1
                y = 0
            if (self.construction[e] == 2):
                list_case.append(case.Case(x,y,"perso"))
            elif(self.construction[e] == 4):
                list_case.append(case.Case(x,y,"guard"))
            elif (self.construction[e] == 3):
                list_case.append(case.Case(x, y, "object"))
            elif(self.construction[e] == 0):
                list_case.append(case.Case(x, y, "ground"))
            else:
                list_case.append(case.Case(x, y, "wall"))
            y +=1

        return list_case

    #affichage des elements de la board
    def showing_board(self):
        for e in self.list_case:
                if(e.case_content == "perso"):
                    print("o", end='')
                elif(e.case_content == "object"):
                    print("=", end='')
                elif (e.case_content == "guard"):
                    print("@", end='')
                elif(e.case_content == "ground"):
                    print("_", end='')
                else:
                    if(e.latitude == self.width-1):
                        print("#")
                    else:
                        print("#", end='')

    def anoucement(self):
        print("width = {} / height = {}".format(self.width,self.height))
        for e in self.list_case:
            print(str(e.longitude) + str(e.latitude) + e.case_content)

    def get_listCase(self):
        return self.list_case