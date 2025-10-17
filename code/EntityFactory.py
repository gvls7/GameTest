from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Player import Player


class EntityFactory:


    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'LVL1-':
                list_bg = []
                for i in range(4):
                    list_bg.append(Background(f'LVL1-{i}', (0,0)))
                    list_bg.append(Background(f'LVL1-{i}', (2400, 0)))
                return list_bg
            case 'Player':
                return Player('Player', (10, WIN_HEIGHT/2))

