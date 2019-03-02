"""

Main Module for the PyGame test

"""

import pygame
from objects import Player


def main():
    """
    Main function of the game
    """

    debug = False
    pygame.init()
    win = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("First Game")

    player = Player(x=50, y=50,
                    width=40, height=60,
                    velocity=15)

    running = True

    while running:
        pygame.time.delay(100)

        for event in pygame.event.get():

            if debug:
                print(event)

            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
                running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            if player.x >= 0:
                player.x -= player.velocity
        if keys[pygame.K_RIGHT]:
            if player.x+player.width <= 500:
                player.x += player.velocity
        if keys[pygame.K_UP]:
            if player.y >= 0:
                player.y -= player.velocity
        if keys[pygame.K_DOWN]:
            if player.y+player.height <= 500:
                player.y += player.velocity

        win.fill((0, 0, 0))
        pygame.draw.rect(win, (255, 0, 0), player.get())
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
