import tkinter as tk

class Game:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("500x500")
        self.create_field()

        self.window.mainloop()

    def create_field(self):
         for i in range(5):
            line = []
            for j in range(5):
                lb = tk.Label(self.window, text = '',
                              width=5, borderwidth=2, relief='ridge')
                lb.grid(row = i, column = j)
        
if __name__ == '__main__':
    game = Game()
