import pygame

from DrawingClass import Drawing
from EnemyClass import Enemy
from GameClass import Game
from PlayerClass import Player
from settings import WIDTH, HEIGHT


def main():
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Space Shooter')
    clock = pygame.time.Clock()

    drawing = Drawing(window)
    enemies = Enemy(1).create(5)
    game = Game(pygame.font.SysFont('comicsans', 30), 60, 3, window, WIDTH, HEIGHT, clock=clock)
    player = Player(WIDTH / 2, HEIGHT - 100, 5, 5)

    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        player.create_bullets()
        player.cooldown()
        player.move()
        game.reload_bullet(len(player.bullets))

        for enemy in enemies:
            enemy.move()

        drawing.drawing(game, player, enemies, 60)

    pygame.quit()


if __name__ == "__main__":
    main()
