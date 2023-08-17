from sprite import Sprite


class Box(Sprite):
    def __init__(self, startx, starty):
        super().__init__("sprites/box.png", startx, starty)