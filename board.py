from typing import Any
from constants import *
from characters import *

board_rect_list = [[[] for i in range(6)] for i in range(6)]
board = [[[] for i in range(6)] for i in range(6)]
character_slots = []
selection_list = pygame.sprite.Group()

def draw_board():
    global board_rect_list
    x, y =  BOARDSTART
    for col in range(COLS):
        for row in range(ROWS):
            if row % 2 == 0 and col % 2 == 0 or row % 2 == 1 and col % 2 == 1:
                board_rect_list[col][row] = []
                board_rect_list[col][row].append(pygame.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE))
                pygame.draw.rect(SCREEN, GREY, (x, y, SQUARE_SIZE, SQUARE_SIZE))
                x += SQUARE_SIZE
            else:
                board_rect_list[col][row] = []
                board_rect_list[col][row].append(pygame.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE))
                pygame.draw.rect(SCREEN, WHITE, (x, y, SQUARE_SIZE, SQUARE_SIZE))
                x += SQUARE_SIZE
            if x >= BOARDEND[0]:
                x = BOARDSTART[0] 
                y += SQUARE_SIZE

def draw_character_slots():
    x, y = CHARACTERSTART
    for slot in range(10):
        character_slot_rect = pygame.Rect((x, y), (SQUARE_SIZE, SQUARE_SIZE))
        character_slots.append(character_slot_rect)
        x += SQUARE_SIZE

def place_characters_in_slots():
    for count, character in enumerate(all_characters):
        setattr(character, "rect", character_slots[count])
        SCREEN.blit(character.image, character.rect)
        pygame.sprite.Group.add(selection_list, character)

def trash_bin():
    trash_rect = pygame.Rect(WIDTH/1.2, HEIGHT/1.2, SQUARE_SIZE, SQUARE_SIZE)
    pygame.draw.rect(SCREEN, RED, (trash_rect))
    return trash_rect
