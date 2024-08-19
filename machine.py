from reel import *
from settings import *
import pygame


class Machine:
    def __init__(self) -> None:
        self.display_surface = pygame.display.get_surface()
        self.reel_index = 0
        self.reel_list = {}

        self.spawn_reels()

    def spawn_reels(self):
        if not self.reel_list:
            x_topleft, y_topleft = 10, -300
        while self.reel_index < 5:
            if self.reel_index == 0:
                x_topleft += 143 
            elif self.reel_index == 1:
                x_topleft -= 143 
            elif self.reel_index == 2:
                x_topleft -= 143
            elif self.reel_index == 3:
                x_topleft -= 143 
            elif self.reel_index == 4:
                x_topleft -= 143 
            self.reel_list[self.reel_index] = Reel((x_topleft, y_topleft))
            x_topleft += 300
            self.reel_index += 1

    def update(self,delta_time):
        for reel in self.reel_list:
            self.reel_list[reel].symbol_list.draw(self.display_surface)
            self.reel_list[reel].symbol_list.update()
