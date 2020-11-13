import sys

import pygame
import pygame.freetype


def create_surface_with_text(text, font_theme, font_size, text_rgb, bg_rgb):
    """ Returns surface with text written on """
    font = pygame.freetype.Font(font_theme, font_size)
    surface, _ = font.render(text=text, fgcolor=text_rgb, bgcolor=bg_rgb)
    return surface.convert_alpha()


def check_events_title(screen, settings):
    """ Sprawdza kursor myszki """
    mouse_up = False
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            mouse_up = True
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(settings.bg_rgb)
    return mouse_up


def title_screen(screen, settings, start_btn, quit_btn):
    """ Zwraca tytułowy ekran gry z menu głównym"""
    # lista przycisków w menu głównym
    buttons = [start_btn, quit_btn]
    while True:
        mouse_up = check_events_title(screen, settings)

        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action
            button.draw(screen)

        pygame.display.flip()

#TODO
# nie dziala
# def check_events_play_game(snake):
#     for event in pygame.event.get():
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_RIGHT:
#                 snake.rect.centerx += 1


def play_level(screen, settings, snake, return_btn):
    """ Zwraca ekran gry po kliknięciu nowej gry"""
    # tą pętle while trzeba wyciągnąć z tego jako osobną funkcję, bo jest taka sama jak w title screen
    while True:
        mouse_up = check_events_title(screen, settings)
        # check_events_play_game(snake)

        #TODO
        # Przycisk powrotu do menu głównego
        # ui_action = return_btn.update(pygame.mouse.get_pos(), mouse_up)
        # if ui_action is not None:
        #     return ui_action
        # return_btn.draw(screen)

        snake.draw_snake()

        pygame.display.flip()
