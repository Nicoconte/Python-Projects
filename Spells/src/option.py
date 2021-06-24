class Options():
    width: int
    height: int
    terminal_color: str
    player_icon: str

    def __init__(self, w=30, h=25, tc="", pi="$") -> None:
        self.width = w
        self.height = h
        self.terminal_color = tc
        self.player_icon = pi