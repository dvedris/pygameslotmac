from settings import *
import pygame, random

class Reel:
    def __init__(self, pos):
        self.symbol_list = pygame.sprite.Group()
        self.shuffled_keys = list(symbols.keys())
        random.shuffle(self.shuffled_keys)
        self.shuffled_keys = self.shuffled_keys[:5] # Only matters when there are more than 5 symbols

        self.reel_is_spinning = False

        pos = list(pos)
        margin = 110
        initial_y = margin + 150
        row_spacing = 50
        for idx, item in enumerate(self.shuffled_keys):
            self.symbol_list.add(Symbol(symbols[item], (pos[0], initial_y), idx))
            initial_y += 50 + row_spacing
class Symbol(pygame.sprite.Sprite):
    def __init__(self, pathToFile, pos, idx):
        super(). __init__()
        
        #Friendly name
        self.sym_type = pathToFile.split('/')[3].split('.')[0]

        self.pos = pos
        self.idx =idx
        self.image = pygame.image.load(pathToFile).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.x_val = self.rect.left

    def update(self):
        pass

