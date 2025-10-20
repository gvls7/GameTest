import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import C_WHITE, WIN_WIDTH, WIN_HEIGHT, ENEMY_EVENT, EVENT_TIMEOUT
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:

    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int]):
        self.timeout = 60000
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('LVL1-'))
        player = EntityFactory.get_entity('Player')
        player.score = player_score[0]
        self.entity_list.append(player)
        pygame.time.set_timer(ENEMY_EVENT, 1200)
        pygame.time.set_timer(EVENT_TIMEOUT, 100)


    def run (self, player_score: list[int]):
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
                if ent.name == 'Player':
                    self.level_text(15, f' Health: {ent.health} | Score: {ent.score}', C_WHITE, (90, 15))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == ENEMY_EVENT:
                    choice = random.choices(['Enemy1', 'Enemy2'], weights = [60, 40], k=1)[0]
                    self.entity_list.append(EntityFactory.get_entity(choice))
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= 100
                    if self.timeout == 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'Player':
                                player_score[0] = ent.score
                        self.show_win_screen()
                        return True

                found_player = False
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        found_player = True

                if not found_player:
                    self.show_lose_screen()
                    return False


            # Tempo restante de jogo
            self.level_text(25, f' Tempo restante: {self.timeout / 1000: .1f}s', C_WHITE, (WIN_WIDTH/2, 15))
            pygame.display.flip()
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)



    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Comic Sans MS", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_pos)
        self.window.blit(source=text_surf, dest=text_rect)

    def show_win_screen(self):
        while True:
            self.window.fill((0, 0, 0))
            self.level_text(60, "You Win!!", C_WHITE, (WIN_WIDTH / 2, WIN_HEIGHT / 2 - 50))
            self.level_text(30, "Press ENTER to continue", C_WHITE, (WIN_WIDTH / 2, WIN_HEIGHT / 2 + 50))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return
            pygame.display.flip()


    def show_lose_screen(self):
        while True:
            self.window.fill((0, 0, 0))
            self.level_text(60, "You Lose", C_WHITE, (WIN_WIDTH / 2, WIN_HEIGHT / 2 - 50))
            self.level_text(30, "Press ENTER to return to menu", C_WHITE, (WIN_WIDTH / 2, WIN_HEIGHT / 2 + 50))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return
            pygame.display.flip()