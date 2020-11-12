import pygame

from pygame.sprite import Sprite
from functions import create_surface_with_text


class UIElement(Sprite):
    """ An user interface element that can be added to a surface """

    def __init__(self, settings, text, center_position, action=None):
        super(UIElement, self).__init__()
        self.settings = settings
        self.action = action
        self.mouse_over = False  # indicates if the mouse is over the element

        # create the default image
        default_image = create_surface_with_text(text, settings.font_theme, settings.font_size, settings.text_rgb,
                                                 settings.bg_rgb)

        # create the image that shows when mouse is over the element
        highlighted_image = create_surface_with_text(text, settings.font_theme, settings.font_size * 1.2,
                                                     settings.text_rgb, settings.bg_rgb)

        # add both images and their rects to lists
        self.images = [default_image, highlighted_image]
        self.rects = [default_image.get_rect(center=center_position),
                      highlighted_image.get_rect(center=center_position)]

    @property
    def image(self):
        return self.images[1] if self.mouse_over else self.images[0]

    @property
    def rect(self):
        return self.rects[1] if self.mouse_over else self.rects[0]

    def update(self, mouse_pos, mouse_up):
        """Updates the element's appearance depending on the mouse position
        and returns the button's action if clicked. """
        if self.rect.collidepoint(mouse_pos):
            self.mouse_over = True
            if mouse_up:
                return self.action
        else:
            self.mouse_over = False

    def draw(self, surface):
        """ Draws element onto a surface """
        surface.blit(self.image, self.rect)