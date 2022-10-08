import random

from game.sprite import Sprite
from game.color import Color
from game.point import Point

class Falling_Object(Sprite):
    '''
        An object falling from the sky.
        The responsibility of Falling_object is to provide random position and random color
    '''
    def __init__(self):
        super().__init__()
        self.set_font_size(30)
    
    def set_rndm_pos (self):
        '''
        Generate a random position in the top of the grid.
        '''
        x = random.randint(1, 30 - 1)
        y = 0
        position = Point(x, y)
        position = position.scale(30)
        self._position = position

    def set_rndm_colr(self):
        '''
        Generates a random color.
        '''
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        self._color = color
