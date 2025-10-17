from code.Const import WIN_WIDTH, ENEMY_SPEED
from code.Entity import Entity


class Enemy(Entity):


    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        self.rect.centerx -= ENEMY_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH