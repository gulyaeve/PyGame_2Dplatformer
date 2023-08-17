from sprite import Sprite


class Player(Sprite):
    def __init__(self, startx, starty):
        super().__init__("sprites/player/P1.png", startx, starty)

