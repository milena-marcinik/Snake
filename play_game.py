import pygame, sys

import functions as func
from settings import Settings
from ui_element import UIElement
from game_state import GameState
from snake_player import Snake

def main():
    pygame.init()
    settings = Settings()  # utworzenie obiektu ustawien
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))  # wymiary ekranu gry
    pygame.display.set_caption("Snake")

    # utworzenie przycisku startowego
    start_btn = UIElement(settings, "Start Game", (screen.get_rect().centerx, screen.get_rect().centery - 20),
                          action=GameState.NEWGAME)
    # utworzenie przycisku wyjścia
    quit_btn = UIElement(settings, "Quit", (screen.get_rect().centerx, screen.get_rect().centery + 30),
                         action=GameState.QUIT)

    # utworzenie przycisku powrotu do menu głównego
    return_btn = UIElement(settings, "Return to main menu",
                           (screen.get_rect().left + 240, screen.get_rect().bottom - 40),
                           action=GameState.TITLE)

    # make a snake
    snake = Snake(screen, settings)

    game_state = GameState.TITLE  # początkowy stan gry

    # main loop
    while True:
        if game_state == GameState.TITLE: # ekran tytułowy
            game_state = func.title_screen(screen, settings, start_btn, quit_btn)

        if game_state == GameState.NEWGAME: # ekran po kliknieciu nowej gry
            game_state = func.play_level(screen, settings, snake, return_btn)

        if game_state == GameState.QUIT: # zamknięcie gry
            pygame.quit()
            return

        pygame.display.update()


if __name__ == '__main__':
    main()
