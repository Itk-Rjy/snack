import tkinter as tk
from threading import Timer
from setting import *
from snake import *
from food import *

class Game:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry(f"{WIDTH_SCREEN}x{HEIGHT_SCREEN}")
        self.field = []
        self.create_field()
        self.run = tk.BooleanVar()
        self.run.set(True)
        self.run.trace_add('write',  self.check_run)
        self.snake = Snake(self, (2, 3), self.field)
        self.window.bind('<Down>', self.press_down)
        self.window.bind('<Up>', self.press_up)
        self.window.bind('<Right>', self.press_right)
        self.window.bind('<Left>', self.press_left)
        self.food = Food(self.field)
        self.start_game()

        self.window.mainloop()

    def change_pos(self):
        if self.run.get():
            self.snake.key_press()
            self.window.update()
            self.window.title(f'score: {len(self.snake.body)}')
            Timer(SPEED, self.change_pos).start()
        
    def press_down(self, event):
        self.snake.walk = [1, 0]
        self.change_pos()

    def press_up(self, event):
        self.snake.walk = [-1, 0]
        self.change_pos()

    def press_right(self, event):
        self.snake.walk = [0, 1]
        self.change_pos()

    def press_left(self, event):
        self.snake.walk = [0, -1]
        self.change_pos()
        
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
        for i in range(HEIGHT):
            for j in range(WIDTH):
                self.field[i][j]['background'] = COLOR_FIELD
        self.snake.drawing_snake()
        self.food.draw_food()
        Timer(SPEED, self.change_pos).start()

    def check_run(self, *args):
        window = tk.Toplevel()
        window.title("GAME OVER")
        window.geometry("250x200")
        restart_button = tk.Button(window, text="Перезапустить игру",
                                  command=lambda: self.dismiss(window, 0))
        restart_button.pack(padx = 10, pady = 10, expand=1)
        close_button = tk.Button(window, text="Завершить игру",
                                  command=lambda: self.dismiss(window, 1))
        close_button.pack(padx = 10, pady = 10, expand=1)
        window.grab_set()

    def dismiss(self, window, choise):
        if choise == 0:
            self.snake.head = [WIDTH//2, HEIGHT//2]
            self.snake.body = []
            del self.run
            self.run = tk.BooleanVar()
            self.run.set(True)
            self.run.trace_add('write',  self.check_run)
            self.start_game()
        elif choise == 1:
            self.window.destroy()
        self.window.update()
        window.grab_release() 
        window.destroy()
      
if __name__ == '__main__':
    game = Game()
