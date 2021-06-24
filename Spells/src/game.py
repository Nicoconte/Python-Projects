import os
import time

from .map import Map
from .option import Options
from .player import Player
from .ui import UI

class Game():

    game_map: Map = None
    player: Player = None 
    ui: UI

    game_state: str

    def __init__(self):
        self.game_map = Map(30, 30)
        self.player = Player("?", self.game_map.width // 2 - 1, self.game_map.height // 2 - 1)
        self.ui = UI()

    def render(self):
        for i in range(len(self.game_map.map)):
            for j in range(len(self.game_map.map[i])):
                print("%3s" %self.game_map.map[i][j], end="")
            print()

    def update(self): 

        os.system('cls')

        self.game_map.generate_map()
        self.game_map.draw_on_map(self.player.player_pos_x, self.player.player_pos_y, self.player.player_sprite)
        self.game_map.set_map_borders()
        self.game_map.draw_items_on_map()
        
        while True:
            
            if self.player.player_life <= 0:
                break
            
            self.player.player_movement(self.game_map)
            self.ui.build_ui(self.player, self.game_map.items_on_map)            
            self.render()            

            time.sleep(1./25)

            os.system('cls')

    staticmethod
    def start(self):
        self.update()

