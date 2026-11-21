import pygame

import assets


class Game:
    def __init__(self, font, FPS, lives, window, screen_width, screen_height, bullets=0, clock=pygame.time.Clock()):
        self.font = font
        self.HEIGHT = screen_height
        self.WIDTH = screen_width
        self.FPS = FPS
        self.lives = lives
        self.level = 1
        self.count = 0
        self.window = window
        self.clock = clock
        self.bullets = bullets
        self.bullet_img = assets.load('bullet_image.png')

    def escape(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        return False

    def over(self):
        if self.lives <= 0:
            label = self.font.render('GAME OVER', 1, (255, 255, 255))
            self.window.blit(label, (self.WIDTH / 2 - label.get_width() / 2, self.HEIGHT / 2 - label.get_height() / 2))
            pygame.display.update()
            for _ in range(self.FPS * 3):
                self.clock.tick(self.FPS)
                pygame.event.pump()
            return True
        return False

    def reload_bullet(self, bullet):
        self.bullets = bullet

    def draw_HUD(self):
        lives_label = self.font.render(f'Lives: {self.lives}', 1, (255, 255, 255))
        level_label = self.font.render(f'Level: {self.level}', 1, (255, 255, 255))
        self.window.blit(lives_label, (10, 10))
        self.window.blit(level_label, (self.WIDTH - level_label.get_width() - 10, 10))
        for i in range(self.bullets):
            x = self.WIDTH - (i + 1) * (self.bullet_img.get_width() + 5) - 10
            self.window.blit(self.bullet_img, (x, self.HEIGHT - 50))
