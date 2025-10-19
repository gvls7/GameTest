import pygame

# C
C_WHITE = (255, 255, 255)
C_OPTION = (255, 253, 85)

# E
ENEMY_EVENT = pygame.USEREVENT + 1
ENTITY_SPEED = {'Enemy1': 6,
                'Enemy2': 4,
                'Player': 7,
                'PlayerShot': 4,
                'Enemy1Shot': 9,
                'Enemy2Shot': 8,
               }

ENTITY_HEALTH = {
    'LVL1-0': 999,
    'LVL1-1': 999,
    'LVL1-2': 999,
    'LVL1-3': 999,
    'Player': 300,
    'Enemy1': 60,
    'Enemy2': 90,
    'PlayerShot': 1,
    'Enemy1Shot': 1,
    'Enemy2Shot': 1,
}

ENTITY_SHOT_DELAY = {
    'Player': 20,
    'Enemy1': 30,
    'Enemy2': 60,
}

ENTITY_DAMAGE = {
    'LVL1-0': 0,
    'LVL1-1': 0,
    'LVL1-2': 0,
    'LVL1-3': 0,
    'Player': 1,
    'PlayerShot': 25,
    'Enemy1': 5,
    'Enemy2': 6,
    'Enemy1Shot': 20,
    'Enemy2Shot': 35,
}

ENTITY_SCORE = {
    'LVL1-0': 0,
    'LVL1-1': 0,
    'LVL1-2': 0,
    'LVL1-3': 0,
    'Player': 0,
    'PlayerShot': 0,
    'Enemy1': 100,
    'Enemy2': 150,
    'Enemy1Shot': 0,
    'Enemy2Shot': 0,
}

# M
MENU_OPTION = ('New Game',
               'Score',
               'Exit')

# W
WIN_WIDTH = 1280
WIN_HEIGHT = 720

