import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class AvoidCollisionAction(Action):
    '''
    An update action that handles interactions between the actors.
    
    The responsibility of AvoidCollisionAction is toavoid that the cycles run into each other when the game is over.

    '''
    def execute(self, cast, script):
        '''
        Chack if the cycles are too close, less than a cell distant, and change the direction of the cycles.
        '''
        turn = False
        cycles = cast.get_actors("cycles")
        head_cycle_0 = cycles[0].get_segments()[0]
        head_cycle_1 = cycles[1].get_segments()[0]
        body_cycle_0 = cycles[0].get_segments()[1:]
        body_cycle_1 = cycles[1].get_segments()[1:]
        #Check distance of cycles from each other
        for segment in body_cycle_0:
            if head_cycle_1.get_position().too_close(segment.get_position()):
                turn = True
        for segment in body_cycle_1:
            if head_cycle_0.get_position().too_close(segment.get_position()):
                turn = True
        #Change direction to avoid collision
        if turn:
            direction_0 = Point(-constants.CELL_SIZE, 0)
            direction_1 = Point(constants.CELL_SIZE, 0)
            cycles[0].turn_head(direction_0)
            cycles[1].turn_head(direction_1)