import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import C_WHITE, WIN_WIDTH, WIN_HEIGHT
from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:

    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('LVL1-'))
        self.entity_list.append(EntityFactory.get_entity('Player'))
        self.timeout = 35000 # 35 segundos


    def run (self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Tempo restante de jogo
            self.level_text(25, f' Tempo restante: {self.timeout / 1000: .1f}s', C_WHITE, (WIN_WIDTH/2, 15))
            pygame.display.flip()


    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Comic Sans MS", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_pos)
        self.window.blit(source=text_surf, dest=text_rect)