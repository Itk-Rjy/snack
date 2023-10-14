from setting import *


class Snake:
    def __init__(self, game, pos, field):
        self.game = game
        self.head = list(pos)
        self.field = field
        self.body = []
        self.walk = [0, 0]

    def drawing(self, coord, color = RED):
        self.field[coord[0]][coord[1]]['background'] = color
        

    def drawing_snake(self):
        self.drawing(self.head, RED)
        for i  in range(len(self.body)):
            self.drawing(self.body[i], GREEN)
        if len(self.body) > 0:
            self.drawing(self.body[-1], COLOR_FIELD)
    
    def key_press(self):
        change = self.walk
        x = self.head[0]+change[0]
        y = self.head[1]+change[1]
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT or\
            self.field[x][y]['background'] == GREEN:
            self.game.run.set(False)
            return
        x = min(WIDTH-1, max(0, self.head[0]+change[0]))
        y = min(HEIGHT-1, max(0, self.head[1]+change[1]))
        if self.field[x][y]['background'] != GREEN and\
            (self.head[0] != x or self.head[1] != y):
            self.body.insert(0, (self.head[0], self.head[1]))
            self.head[0] = x
            self.head[1] = y  
            if self.field[x][y]['background'] == COLOR_FOOD:
                self.body.append(self.body[-1])
                self.game.food.new_coords()
                self.game.food.draw_food()
            self.drawing_snake()
            
            self.body.pop(-1)
            

    
        
