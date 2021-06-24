import json
import os

class Colors():
    colors = {
        "red": "\033[1;31;40m",
        "green": "\033[1;32;40m",
        "yellow": "\033[1;33;40m",
        "blue": "\033[1;34;40m",
        "magenta": "\033[1;35;40m",
        "cyan": "\033[1;36;40m"
    }


def load_items():
    items = None
    current_path = os.getcwd()
    with open(f"{current_path}/src/assets/items.json") as file:
        items = json.load(file)
    return items