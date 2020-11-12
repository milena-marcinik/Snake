import sys

import pygame
import pygame.freetype


def create_surface_with_text(text, font_theme, font_size, text_rgb, bg_rgb):
    """ Returns surface with text written on """
    font = pygame.freetype.Font(font_theme, font_size)
    surface, _ = font.render(text=text, fgcolor=text_rgb, bgcolor=bg_rgb)
    return surface.convert_alpha()


def title_screen(screen, settings, start_btn, quit_btn):
    buttons = [start_btn, quit_btn]
    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(settings.bg_rgb)

        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action
            button.draw(screen)

        pygame.display.flip()


def play_level(screen, settings, return_btn):
    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(settings.bg_rgb)

        ui_action = return_btn.update(pygame.mouse.get_pos(), mouse_up)
        if ui_action is not None:
            return ui_action
        return_btn.draw(screen)

        pygame.display.flip()
