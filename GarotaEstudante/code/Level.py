#!/usr/bin/python
#coding: Utf-8 *-*

import pygame

from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:

    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode

        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))

    def run(self):

        clock = pygame.time.Clock()

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            bg1 = self.entity_list[0]
            bg2 = self.entity_list[1]

            #bg1.move() #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx quando tiver Player pra mover cenário
            #bg2.move() #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx quando tiver Player pra mover cenário

            if bg1.rect.right <= 0:
                bg1.rect.left = bg2.rect.right

            if bg2.rect.right <= 0:
                bg2.rect.left = bg1.rect.right

            self.window.blit(source=bg1.surf,
                             dest=bg1.rect)

            self.window.blit(source=bg2.surf,
                             dest=bg2.rect)

            pygame.display.flip()

            clock.tick(60)
