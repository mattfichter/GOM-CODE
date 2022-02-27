from cmath import rect
import pygame
from characters import *
from board import *


class Sprite_Mouse_Location(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.rect = pygame.Rect(x,y,1,1)

def select_character():
    x, y = pygame.mouse.get_pos()
    for character in selection_list:
        is_selected = False
        if character.rect.colliderect(Sprite_Mouse_Location(x, y).rect):
            is_selected = True