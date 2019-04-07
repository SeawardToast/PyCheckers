class Checker_Board:
    def __init__(self):
        self.board_arr = []
        self.u = 10
        for x in range(0,8):
            self.board_arr.insert(x, [0, 0, 0, 0, 0, 0, 0, 0])
        for r in range(0,8):
            for t in range(0,8):
                temp = t%2
                if(r == 0 and temp == 0 or r == 2 and temp == 0):
                    self.board_arr[r][t] = 2
                if(r == 1 and temp != 0):
                    self.board_arr[r][t] = 2

                if(r == 5 and temp != 0 or r == 7 and temp != 0):
                    self.board_arr[r][t] = 1
                if(r == 6 and temp == 0):
                    self.board_arr[r][t] = 1
