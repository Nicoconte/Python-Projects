from .utils import *
from .items import Item

import random

class Map():
    width: int
    height: int 
    sprite: str
    border_sprite: str #aka border
    items: dict
    spawn_time: int

    items_on_map: list
    
    map: list

    def __init__(self, w, h, gs=".", lt="#"):
        self.width = w
        self.height = h
        self.sprite = gs
        self.border_sprite = lt
        self.map = []
        self.items_on_map = []
        self.spawn_time = random.randint(1, 20)

    def generate_map(self):
        for i in range(self.height):
            self.map.append([self.sprite] * self.width)
        return self.map

    def draw_on_map(self, x, y, thing_to_draw):
        self.map[y][x] = thing_to_draw  
        return self.map

    def set_map_borders(self):
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if i == 0:
                    self.map[0][j] = self.border_sprite
                elif i == self.height - 1:
                    self.map[i][j] = self.border_sprite
                else:   
                    self.map[i][ self.width - 1 ] = self.border_sprite
                    self.map[i][0] = self.border_sprite        
                    
        return self.map

    def draw_items_on_map(self):
        current_item = None

        for i in range(self.spawn_time):
            current_item = Item().get_random_item(self.width, self.height)
            self.draw_on_map(current_item.x, current_item.y, current_item.sprite)    
            self.items_on_map.append(current_item)

        return self.map
