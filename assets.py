import os

import pygame

IMG_DIR = os.path.join(os.path.dirname(__file__), 'img')


def load(name):
    return pygame.image.load(os.path.join(IMG_DIR, name))
