import pygame.key

from sprite import Sprite


class Player(Sprite):
    def __init__(self, startx, starty):
        super().__init__("sprites/player/P1.png", startx, starty)

        self.speed = 4
        self.jump = 20
        self.gravity = 1
        self.vertical_speed = 0

    def update(self, boxes) -> None:
        horizontal_speed = 0
        onground = pygame.sprite.spritecollideany(self, boxes)

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            horizontal_speed = -self.speed
        if key[pygame.K_RIGHT]:
            horizontal_speed = self.speed
        if key[pygame.K_UP] and onground:
            self.vertical_speed = -self.jump
        if self.vertical_speed < 10 and not onground:
            self.vertical_speed += self.gravity
        if self.vertical_speed > 0 and onground:
            self.vertical_speed = 0

        self.move(horizontal_speed, self.vertical_speed)

    def move(self, x, y):
        self.rect.move_ip([x, y])

