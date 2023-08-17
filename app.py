import sys

import pygame

from box import Box
from player import Player

WIDTH = 400
HEIGHT = 300
BACKGROUND = (0, 0, 0)


def game():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    player = Player(100, 100)
    boxes = pygame.sprite.Group()
    for box in range(0, 400, 50):
        boxes.add(Box(box, 300))

    while True:
        screen.fill(BACKGROUND)

        player.update(boxes)
        player.draw(screen)
        boxes.draw(screen)

        pygame.display.flip()
        clock.tick(60)  # FPS
        # print(clock.get_fps())

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


if __name__ == '__main__':
    game()
