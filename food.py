from setting import *
import random as rd


class Food:
    def __init__(self, field):
        self.x = rd.randint(0, WIDTH-1)
        self.y = rd.randint(0, HEIGHT-1)
        self.field = field
        

    
    def draw_food(self):
        self.field[self.x][self.y]['background'] = COLOR_FOOD


    def new_coords(self):
        while self.field[self.x][self.y]['background'] != COLOR_FIELD:
            self.x = rd.randint(0, WIDTH-1)
            self.y = rd.randint(0, HEIGHT-1)
