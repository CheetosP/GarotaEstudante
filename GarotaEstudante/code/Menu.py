#!/usr/bin/python
# --coding: utf-8 --

class Menu:

    def _init_(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/menufoto.jpg')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pass
