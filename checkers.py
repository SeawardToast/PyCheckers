import tkinter as tk
import checker_piece
import checker_board

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.p1 = checker_piece.Checker_Piece("normal", "red")
        self.cb = checker_board.Checker_Board()
        self.create_widgets()
    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Start game"
        
        self.hi_there.pack(side="top")

        self.entry = tk.Entry(self)
        self.entry.pack()
        self.hi_there["command"] = self.say_hi
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")
        input = self.entry.get()
        input_arr = input.split(",", 4)
        print(input_arr)
        self.p1.move(input_arr[0], input_arr[1], self.cb)
        print_board(self.cb)

    def print_board(self, board):
        for r in board:
            print(r)

root = tk.Tk()
app = Application(master=root)
app.mainloop()
