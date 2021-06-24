from .player import Player
from .map import Map

class UI():
    gui: str

    def __init__(self):
        self.gui = ""

    def show_life(self, player):
        life = f"life: {player.player_life}"
        return life

    def show_current_pos(self, player):
        position = f"x: {player.player_pos_x} | y: {player.player_pos_y}"
        return position

    def show_options(self):
        option = f"1-Inventory | 2-Stats | 3-Quest" 
        return option

    def build_ui(self, player, inventory):
        self.gui = f"""
  ********************************************************************
  *                                                                  *
  * {self.show_life(player)} -> {self.show_current_pos(player)} -> {self.show_options()}    *                                               
  * 
  *    	                                                             *
  ********************************************************************"""
        print(self.gui)