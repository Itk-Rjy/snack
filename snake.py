from setting import *


class Snake:
    def __init__(self, pos, field):
        self.pos = list(pos)
        self.field = field
        self.body =[]
        self.drawing()

    def drawing(self, color = RED):
        self.field[self.pos[0]][self.pos[1]]['background'] = color

    def key_press(self, change):
        x = min(WIDTH-1, max(0, self.pos[0]+change[0]))
        y = min(HEIGHT-1, max(0, self.pos[1]+change[1]))
        self.drawing(COLOR_FIELD)
        self.pos[0] = x
        self.pos[1] = y  
        if self.field[x][y]['background'] == COLOR_FOOD:
            print('food')
        self.drawing(RED)

    
        
