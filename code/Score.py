import sys
from datetime import datetime

import pygame
from pygame import Surface, Rect, KEYDOWN, K_RETURN, K_BACKSPACE, K_ESCAPE
from pygame.font import Font

from code.Const import C_WHITE, WIN_HEIGHT, WIN_WIDTH, C_OPTION, MENU_OPTION
from code.DBProxy import DBProxy


class Score:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/Score1.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)


    def save_score(self, menu_return: str, player_score: list[int]):
        db_proxy = DBProxy('Score')
        name = ''
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(50, 'Score:', C_OPTION, (WIN_WIDTH / 2, 30))
            if menu_return == MENU_OPTION[0]:
                score = player_score[0]
                text = 'Enter your name (4 characters): '

            self.score_text(40, text, C_WHITE, (WIN_WIDTH / 2, 80))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len(name) == 4:
                        db_proxy.save({'name': name, 'score': score, 'date': get_formatted_date()})
                        self.show_score()
                        return
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 4:
                            name += event.unicode
            self.score_text(30, name, C_WHITE, (WIN_WIDTH / 2, 200))
            pygame.display.flip()


    def show_score(self):
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_text(20, 'TOP SCORE', C_WHITE, (WIN_WIDTH / 2, WIN_HEIGHT / 2))
        header_text = f'{"NAME":<4}                {"SCORE":>5}                         {"DATE":<12}'
        self.score_text(18, header_text, C_OPTION, (WIN_WIDTH / 2, 500))

        db_proxy = DBProxy('Score')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        y_offset = 530
        for i, player_score in enumerate(list_score):
            id_, name, score, date = player_score
            data_text = f'        {name:<4}                    {score:05d}                  {date:<12}'
            self.score_text(18, data_text, C_OPTION, (WIN_WIDTH / 2, y_offset + i * 25))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
            pygame.display.flip()


    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Comic Sans MS", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

def get_formatted_date():
    current_datetime = datetime.now()
    current_date = current_datetime.strftime('%d/%m/%Y')
    current_time = current_datetime.strftime('%H:%M')
    return f'{current_date} {current_time}'