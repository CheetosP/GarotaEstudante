#!/usr/bin/python
# -*- coding: utf-8 -*-
#from _curses import COLOR_YELLOW

import pygame
from pygame import Surface, Rect
from pygame.font import Font
from code.Const import WIN_WIDTH, COLOR_GREEN, MENU_OPTION, COLOR_WHITE, COLOR_YELLOW

class Menu:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/menufoto.jpg')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        menu_option = 0
        pygame.mixer_music.load('./asset/fundopantano.mp3')
        #----pygame.mixer_music.play(-1)

        while True:
            # DRAW IMAGE
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(text_size=130, text="Rwby Aventureira", text_color=COLOR_GREEN, text_center_pos=((WIN_WIDTH / 2), 200))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(text_size=50, text=MENU_OPTION[i], text_color=COLOR_YELLOW, text_center_pos=((WIN_WIDTH / 2), 350 + 50 * i))

                else:
                    self.menu_text(text_size=50, text=MENU_OPTION[i], text_color=COLOR_WHITE, text_center_pos=((WIN_WIDTH / 2), 350 + 50 * i))
            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # End pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN: #down key
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:  # up key
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:  #enter
                        return MENU_OPTION[menu_option]
            pygame.display.flip()

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