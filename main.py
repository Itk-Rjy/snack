import tkinter as tk
from setting import *
from snake import *
from food import *

class Game:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry(f"{WIDTH_SCREEN}x{HEIGHT_SCREEN}")
        self.field = []
        self.create_field()
        self.snake = Snake((2, 3), self.field)
        self.window.bind('<Down>', self.press_down)
        self.window.bind('<Up>', self.press_up)
        self.window.bind('<Right>', self.press_right)
        self.window.bind('<Left>', self.press_left)
        self.food = Food(self.field)
        self.start_game()

        self.window.mainloop()
        
    def press_down(self, event):
        self.snake.key_press([1, 0])
        self.window.update()

    def press_up(self, event):
        self.snake.key_press([-1, 0])
        self.window.update()

    def press_right(self, event):
        self.snake.key_press([0, 1])
        self.window.update()

    def press_left(self, event):
        self.snake.key_press([0, -1])
        self.window.update()
        
    def create_field(self):
         for i in range(HEIGHT):
            line = []
            for j in range(WIDTH):
                lb = tk.Label(self.window, text = '',
                              width=2, borderwidth=2, relief='ridge',
                              background = COLOR_FIELD)
                lb.grid(row = i, column = j)
                line.append(lb)
            self.field.append(line)
            
    def start_game(self):
        self.food.draw_food()
 
        
if __name__ == '__main__':
    game = Game()
