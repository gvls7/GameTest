import pygame

# C
C_WHITE = (255, 255, 255)
C_OPTION = (255, 253, 85)

# E
ENEMY_EVENT = pygame.USEREVENT + 1
ENEMY_SPEED = {'Enemy1' : 9,
               'Enemy2' : 6,
               }

ENTITY_HEALTH = {
    'LVL1-0': 999,
    'LVL1-1': 999,
    'LVL1-2': 999,
    'LVL1-3': 999,
    'Player': 100,
    'Enemy1': 15,
    'Enemy2': 2,
}

# M
MENU_OPTION = ('New Game',
               'Score',
               'Exit')

# W
WIN_WIDTH = 1280
WIN_HEIGHT = 720

