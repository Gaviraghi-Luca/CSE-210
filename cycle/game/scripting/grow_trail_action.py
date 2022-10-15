import constants
from game.scripting.action import Action

class GrowTrailAction(Action):
    '''

    '''
    def __init__(self):
        self._counter = 0

    def execute(self, cast, script):
        self._counter += 1
        cycles = cast.get_actors("cycles")
        if (self._counter % 100) == 0:
                cycles[0].grow_trail(1, constants.RED)
                cycles[1].grow_trail(1, constants.FUCSIA)