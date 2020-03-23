import case

class Board:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.list_case = self.initialize()

    def initialize(self):
        list_case = []
        x = 0
        y = 0
        for e in range(self.width*self.height):
            if y == self.width:
                x +=1
                y = 0
            if (x == 0) or (y == 0) or (x == self.height-1) or (y == self.width-1):
                list_case.append(case.Case(x,y,"wall"))
            else:
                list_case.append(case.Case(x,y,"ground"))
            y +=1
        return list_case

    def showing_board(self):
        for e in self.list_case:
            if(e.case_content == "perso"):
                print("o")
            elif(e.case_content == "object"):
                print("=")
            elif(e.case_content == "ground"):
                print("_")
            else:
                print("$")
    def anoucement(self):
        print("width = {} / height = {}".format(self.width,self.height))
        for e in self.list_case:
            print(str(e.longitude) + str(e.latitude) + e.case_content)

