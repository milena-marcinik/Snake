import pygame


class Snake:
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, settings.snake_width, settings.snake_height)
        self.screen_rect = screen.get_rect()

        # Start each new ship at the center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        # Store a decimal value for the ship's center.
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.color = settings.snake_rgb
        self.speed_factor = settings.snake_speed_factor

    def update(self):
        """Update the snake's position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.speed_factor
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.speed_factor
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.speed_factor

        # Update rect object from self.center
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def center_snake(self):
        self.centerx = self.screen_rect.centerx
        self.centery = self.screen_rect.centery

    def draw_snake(self):
        """Draw the snake at its current location."""
        pygame.draw.rect(self.screen, self.color, self.rect)
