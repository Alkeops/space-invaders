import pygame

import assets


class Drawing:
    def __init__(self, window):
        self.window = window
        self.background = assets.load('background.png')

    def drawing(self, game, player, enemies, FPS):
        self.window.blit(self.background, (0, 0))
        player.fire(self.window)
        for enemy in enemies[:]:
            enemy.draw(self.window)
        player.draw(self.window)
        game.draw_HUD()
        pygame.display.update()
