import pygame
from constants import ARCHERIMAGE, BOXERIMAGE, BRUTEIMAGE, CANNONIMAGE, COMMONERIMAGE, DIAGONALIMAGE, MIMICIMAGE, NINJAIMAGE, SUPPORTIMAGE, TRANSPORTERIMAGE

class Character(pygame.sprite.Sprite):
    def __init__(self, image, rect, identity, level, health, index):
        super().__init__()
        self.image = image
        self.rect = rect
        self.identity = identity
        self.level = level
        self.health = health
        self.index = index
        self.buff = False 
        self.killable = False
        self.team = ["One", "Two"]

brute = Character(BRUTEIMAGE, None, "brute", 4, 3, 0)
cannon = Character(CANNONIMAGE, None, "cannon", 4, 3, 1)
archer = Character(ARCHERIMAGE, None, "archer", 3, 2, 2)
boxer = Character(BOXERIMAGE, None, "boxer", 3, 3, 3)
support = Character(SUPPORTIMAGE, None, "support", 3, 2, 4)
diagonal = Character(DIAGONALIMAGE, None, "diagonal", 2, 1, 5)
mimic = Character(MIMICIMAGE, None, "mimic", 2, 2, 6)
ninja = Character(NINJAIMAGE, None, "ninja", 2, 1, 7)
transporter = Character(TRANSPORTERIMAGE, None, "transporter", 2, 1, 8)
commoner = Character(COMMONERIMAGE, None, "commoner", 1, 1, 9)

all_characters = [brute, cannon, archer, boxer, support, diagonal, mimic, ninja, transporter, commoner]