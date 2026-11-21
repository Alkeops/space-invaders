import random

import pygame

import assets
from settings import WIDTH
from ShipClass import Ship


class Enemy(Ship):
    COLOR = {
        'blue': (assets.load('enemy_blue_image.png'), assets.load('shot_blue.png')),
        'green': (assets.load('enemy_green_image.png'), assets.load('shot_green.png')),
        'purple': (assets.load('enemy_purple_image.png'), assets.load('shot_purple.png')),
    }

    def __init__(self, speed, x=50, y=50, color='blue', health=100):
        super().__init__(x, y, health)
        self.ship_img, self.bullet_img = self.COLOR[color]
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.speed = speed

    def move(self):
        self.y += self.speed

    def create(self, amount):
        enemies = []
        enemy_width = self.COLOR['blue'][0].get_width()
        for _ in range(amount):
            enemies.append(Enemy(
                self.speed,
                random.randrange(20, WIDTH - enemy_width - 20),
                random.randrange(-1000, -100),
                random.choice(list(self.COLOR.keys())),
            ))
        return enemies

    def increase_speed(self):
        self.speed *= 1.02
