import case

class Board:

    def __init__(self, width, height):
        self.width = width
        self.height = height

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
        for e in list_case:
            print(str(e.longitude) + str(e.latitude) + e.case_content)
        return list_case

    def anoucement(self):
        print("width = {} / height = {}".format(self.width,self.height))
