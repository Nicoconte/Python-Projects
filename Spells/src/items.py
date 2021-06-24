from .utils import * 

import random

class Item:
    name: str
    sprite:str
    cost: int
    x:int
    y:int

    items_info: dict

    def __init__(self, name=None, sprite=None, cost=None, x=None, y=None) -> None:
        self.name = name
        self.sprite = sprite
        self.cost = cost
        self.x = x
        self.y = y

        self.items_info = load_items()

    staticmethod
    def get_random_item(self, w, h):
        index = random.randint(0, len(self.items_info)) - 1
        keys = list(self.items_info.keys())

        x = random.randint(3, w - 3)
        y = random.randint(3, h - 3)        

        name = self.items_info[keys[index]]
        cost = self.items_info[keys[index]]['cost']
        sprite = self.items_info[keys[index]]['sprite']

        return Item(name, sprite, cost, x, y)
