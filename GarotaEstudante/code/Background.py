#!/usr/bin/python
# -*- coding: utf-8 -*-

#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Entity import Entity


class Background(Entity):

    def __init__(self, name, position):
        super().__init__(name, position)

        # Redimensiona apenas o fundo
        self.surf = pygame.transform.scale(
            self.surf,
            (WIN_WIDTH, WIN_HEIGHT)
        )

        # Atualiza o retângulo mantendo a posição
        self.rect = self.surf.get_rect(
            left=position[0],
            top=position[1]
        )

    def move(self):
        self.rect.x -= 1