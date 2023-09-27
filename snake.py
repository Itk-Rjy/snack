from setting import *


class Snake:
    def __init__(self, pos, field):
        self.head = list(pos)
        self.field = field
        self.body = [(2,4),(2,5),(1,5)]
        self.drawing_snake()

    def drawing(self, coord, color = RED):
        self.field[coord[0]][coord[1]]['background'] = color
        

    def drawing_snake(self):
        self.drawing(self.head, RED)
        for i  in range(len(self.body)):
            self.drawing(self.body[i], GREEN)
    
    def key_press(self, change):
        x = min(WIDTH-1, max(0, self.head[0]+change[0]))
        y = min(HEIGHT-1, max(0, self.head[1]+change[1]))
        #self.drawing(self.head, COLOR_FIELD)
        self.body.insert(0, (self.head[0], self.head[1]))
        self.body.pop(-1)
        self.head[0] = x
        self.head[1] = y  
        if self.field[x][y]['background'] == COLOR_FOOD:
            print('food')
        self.drawing_snake()

    
        
