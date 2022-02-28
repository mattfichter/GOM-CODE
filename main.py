from tkinter import Button
import click
import pygame
from constants import *
from board import *
from characters import *
from teamselection import *
from itertools import chain

clickX = 0
clickY = 0
motionX = 0
motionY = 0
game_phase = 0
FPS = 60
is_selected = False
selected_character = []
dirty_rect_list = []
characters_on_board = pygame.sprite.Group()
pygame.init()
dragging = False
ready = []

def select_character():
    global is_selected, clickX, clickY, characters_on_board
    if is_selected == False:
        for character in selection_list:
            if character.rect.collidepoint(clickX, clickY):
                selected_character.clear()
                selected_character.append(character)
                clickX, clickY = 0, 0
                is_selected = True
        for character in characters_on_board:
            if character.rect.collidepoint(clickX, clickY):
                selected_character.clear()
                selected_character.append(character)
                clickX, clickY = 0, 0
                all_characters.append(character)
                is_selected = True
                pygame.sprite.Group.remove(character)           

def drag_character():
    global clickX, clickY, dragging, is_selected, selected_character
    x, y = pygame.mouse.get_pos()
    if is_selected == True:
        dragging = True
        mouse_rect = pygame.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE)
        mouse_rect.center = (x, y)
        setattr(selected_character[0], "rect", mouse_rect)
        SCREEN.fill(BLACK)
        draw_board()
        trash_bin()
        SCREEN.blit(selected_character[0].image, selected_character[0].rect)
        dragging == True

        if trash_bin().collidepoint(clickX, clickY):
            remove_placed_character_from_board()
            is_selected = False
            dragging = False
            SCREEN.fill(BLACK)
            draw_board()
            pygame.sprite.Group.draw(characters_on_board, SCREEN)
            draw_character_slots()
            place_characters_in_slots()
    if dragging == True:
        place_character_first_row()


def place_character():
    global clickX, clickY, is_selected, dragging
    if is_selected == True:
        for col in (board_rect_list):
            for row in list(col):
                if row[0].collidepoint(clickX, clickY):
                    setattr(selected_character[0], "rect", row[0])
                    SCREEN.fill(BLACK)
                    draw_board()
                    SCREEN.blit(selected_character[0].image, row[0])
                    draw_character_slots()
                    place_characters_in_slots()
                    pygame.display.update()
                    is_selected = False
                    dragging = False

def place_character_first_row():
    global clickX, clickY, is_selected, dragging, selected_character, characters_on_board, all_characters
    if is_selected == True:
        col_list = []
        for rect in board_rect_list[5]:
            if rect[0].collidepoint(clickX, clickY):
                setattr(selected_character[0], "rect", rect[0])
                pygame.sprite.Group.add(characters_on_board, selected_character[0])
                selected_character = []
                remove_placed_character_from_start()
                SCREEN.fill(BLACK)
                draw_board()
                pygame.sprite.Group.draw(characters_on_board, SCREEN)
                draw_character_slots()
                place_characters_in_slots()
                pygame.display.update()
                is_selected = False
                dragging = False

def remove_placed_character_from_start():
    for character in all_characters:
        for characters in characters_on_board:
            if characters.identity == character.identity:
                all_characters.remove(character)

def remove_placed_character_from_board():
    global selected_character
    for character in all_characters:
        for characters in selected_character:
            for x in characters_on_board:
                if characters.identity != character.identity and characters.identity == x.identity:
                    characters_on_board.remove(characters)
                    all_characters.insert(characters.index, characters)
                    selected_character = []

def remove_all_character_from_board():
    for character in all_characters:
        for characters in characters_on_board:
            if characters.identity != character.identity:
                characters_on_board.remove(characters)
                all_characters.insert(characters.index, characters)
                selected_character = []

def sum_levels():
    levels = 0
    for character in characters_on_board:
        levels += character.level
    return levels

def ready_button():
    global ready, clickX, clickY
    if sum_levels() == 10:
        ready_rect = pygame.Rect(WIDTH/1.2, HEIGHT/3, SQUARE_SIZE, SQUARE_SIZE)
        pygame.draw.rect(SCREEN, GREY, ready_rect)
        ready.append(ready_rect)
        if ready[0].collidepoint(clickX, clickY):
            draw_board()
            draw_character_slots()
            remove_all_character_from_board()
            place_characters_in_slots()
    
            

def new_phase():
    global ready, clickX, clickY
    if sum_levels() == 10 and ready[0].collidepoint(clickX, clickY):
        SCREEN.fill(BLACK)
        draw_board()
        draw_character_slots()
        remove_all_character_from_board()
        place_characters_in_slots()

            





def main():
    run = True
    clock = pygame.time.Clock()
    SCREEN 
    draw_board()
    draw_character_slots()
    place_characters_in_slots()

    while run:
        clock.tick(FPS)
        drag_character()
        ready_button()
        pygame.sprite.Group.draw(characters_on_board, SCREEN)
     

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONUP:
                global clickX, clickY
                clickX, clickY = event.pos
                select_character()
                print(characters_on_board)
                print(sum_levels())
                  
            if event.type == pygame.MOUSEMOTION:
                motionX, motionY = event.pos

        pygame.display.update()
main()