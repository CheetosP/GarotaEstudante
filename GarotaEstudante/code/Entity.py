#!/usr/bin/python
#*-* coding: utf-8 *-*
from abc import ABC, abstractmethod

import pygame.image

from code.Const import WIN_WIDTH, WIN_HEIGHT


class Entity(ABC):

    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load(f'./asset/{name}.png').convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (WIN_WIDTH, WIN_HEIGHT))
        self.rect = self.surf.get_rect(left=position[0], top=position[1])  #posição dos inimigos
        self.speed = 0  #velocidade dos inimigos


@abstractmethod
def move(self, ):
    pass
