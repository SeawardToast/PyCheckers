class Checker_Piece:
    def __init__(self, type, team):
        self.type = type
        self.team = team
        self.x = 1
        self.y = 0

        def king():
            print("I am king")
        def normal():
            print("I am normal")

        options = {0 : normal, 1 : king}

    def move(self, destx, desty, board):
        print("selfx: ", self.x, "selfy: ", self.y)
        temp = board[self.x][self.y]
        remx = destx%2
        remy = desty%2
        print("destx: ", destx, "desty: ", desty)
        if(destx-self.x==1 or self.x-destx==1):
            print("You can not move there")
            return
        board[self.x][self.y] = 5
        board[destx][desty] = temp

        

    
