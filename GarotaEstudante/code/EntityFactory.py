"""#!/usr/bin/python
#*_* coding: utf-8 *_*
from code.Background import Background


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg': # background
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'Level1Bg{i}', position))


                return list_bg

            case _:
                return []"""


#!/usr/bin/python
# -*- coding: utf-8 -*-

#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.Background import Background
from code.Const import WIN_WIDTH


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):

        match entity_name:

            case 'Level1Bg':

                return [
                    Background(name='Level1Bg',
                               position=(0, 0)),

                    Background(name='Level2Bg',
                               position=(WIN_WIDTH, 0))
                ]

            case _:
                return []