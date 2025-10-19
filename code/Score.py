import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import C_WHITE, WIN_HEIGHT, WIN_WIDTH, C_OPTION


class Score:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/Score1.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)


    def save_score(self, menu_return: str):
        self.window.blit(source=self.surf, dest=self.rect)
        while True:
            pygame.display.flip()


    def show_score(self):
        self.window.blit(source=self.surf, dest=self.rect)
        while True:
            self.score_text(50, 'Score:', C_OPTION, (WIN_WIDTH / 2, 30))
            self.score_text(20, 'Your name:', C_WHITE, (WIN_WIDTH / 2, WIN_HEIGHT / 2))
            pygame.display.flip()


    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Comic Sans MS", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)