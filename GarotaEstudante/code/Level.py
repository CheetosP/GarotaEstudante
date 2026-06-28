#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import COLOR_WHITE, WIN_HEIGHT
from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:

    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.timeout = 30000  # tempo em milissegundos (30s, pode ajustar)

        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))

    def run(self):
        pygame.mixer_music.load('./asset/praia.mp3')
        pygame.mixer_music.play(-1)

        clock = pygame.time.Clock()
        start_ticks = pygame.time.get_ticks()  # marca o início

        while True:
            elapsed = pygame.time.get_ticks() - start_ticks
            remaining = max(0, (self.timeout - elapsed) / 1000)  # segundos restantes

            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                # ent.move()  # Ativar quando criar o Player

            # Textos da fase
            self.level_text(text_size=14, text=f'{self.name} - Timeout: {remaining:.1f}s', text_color=COLOR_WHITE, text_pos=(10, 5))
            self.level_text(text_size=14, text=f'FPS: {clock.get_fps():.0f}', text_color=COLOR_WHITE, text_pos=(10, WIN_HEIGHT - 35))
            self.level_text(text_size=14, text=f'Entidades: {len(self.entity_list)}', text_color=COLOR_WHITE, text_pos=(10, WIN_HEIGHT - 20))

            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)