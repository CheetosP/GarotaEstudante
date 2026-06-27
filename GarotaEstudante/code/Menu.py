#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from pygame import Surface, Rect
from pygame.font import Font
from code.Const import WIN_WIDTH, COLOR_GREEN, MENU_OPTION, COLOR_WHITE

class Menu:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/menufoto.jpg')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer_music.load('./asset/fundopantano.mp3')
        #--------------------------pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(text_size=130, text="Rwby Aventureira", text_color=COLOR_GREEN, text_center_pos=((WIN_WIDTH / 2), 200))

            for i in range(len(MENU_OPTION)):
                self.menu_text(text_size=50, text=MENU_OPTION[i], text_color=COLOR_WHITE, text_center_pos=((WIN_WIDTH / 2), 350 + 50 * i))

            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # End pygame

#    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
 #       text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
  #      text_font: Font = pygame.font.SysFont("Lucida Sans Typewriter", text_size)
   #     text_rect: Rect = text_surf.get_rect(center=text_center_pos)
    #    self.window.blit(source=text_surf, dest=text_rect)

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
            text_font: Font = pygame.font.SysFont("Impact", text_size)
            text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
            text_rect: Rect = text_surf.get_rect(center=text_center_pos)
            self.window.blit(source=text_surf, dest=text_rect)