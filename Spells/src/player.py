import keyboard
import os

from .map import Map

class Player():
    player_sprite: str
    player_pos_x: int
    player_pos_y: int
    player_life: int
    player_color: str
    player_inventory: list

    def __init__(self, sprite, x, y, life=100):
        self.player_sprite = sprite
        self.player_pos_x = x
        self.player_pos_y = y
        self.player_life = life
        self.player_inventory = []

    def player_movement(self, map: Map):
        x = 0
        y = 0

        if keyboard.is_pressed('a') and not self.is_collided_with(map.width, map.height):
            x = self.player_pos_x - 1 
            y = self.player_pos_y
            map.draw_on_map(x, y, self.player_sprite)
            map.draw_on_map(x + 1, y, map.sprite)
            map.draw_on_map(0, y, map.border_sprite)    
            self.update_player_pos(x, y)                                            

        if keyboard.is_pressed('d') and not self.is_collided_with(map.width, map.height):
            x = self.player_pos_x + 1
            y = self.player_pos_y
            map.draw_on_map(x, y, self.player_sprite)
            map.draw_on_map(x - 1, y, map.sprite)
            map.draw_on_map(map.width - 1, y, map.border_sprite)
            self.update_player_pos(x, y)

        if keyboard.is_pressed('w') and not self.is_collided_with(map.width, map.height):
            x = self.player_pos_x
            y = self.player_pos_y - 1 
            map.draw_on_map(x, y, self.player_sprite)
            map.draw_on_map(x, y + 1, map.sprite)
            map.draw_on_map(x, 0, map.border_sprite)
            self.update_player_pos(x, y)

        if keyboard.is_pressed('s') and not self.is_collided_with(map.width, map.height):
            x = self.player_pos_x 
            y = self.player_pos_y + 1
            map.draw_on_map(x, y, self.player_sprite)
            map.draw_on_map(x, y - 1, map.sprite)
            map.draw_on_map(x, map.height - 1, map.border_sprite)
            self.update_player_pos(x, y)

        return map

    def update_player_pos(self, x, y):
        self.player_pos_x = x
        self.player_pos_y = y  

            
    def is_collided_with(self, object_x, object_y):
        if self.player_pos_x <= 0: 
            self.player_pos_x = self.player_pos_x + 2
            return True
        if self.player_pos_x >= object_x - 1:
            self.player_pos_x = self.player_pos_x - 2
            return True 
        if self.player_pos_y <= 0:
            self.player_pos_y = self.player_pos_y + 2
            return True 
        if self.player_pos_y >= object_y - 1:
            self.player_pos_y = self.player_pos_y - 2
            return True