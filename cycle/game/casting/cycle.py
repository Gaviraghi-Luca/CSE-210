import constants
import random
from game.casting.actor import Actor
from game.shared.point import Point


class Cycle(Actor):
    """
    A long limbless reptile.
    
    The responsibility of Cycle is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self, color):
        super().__init__()
        self._segments = []
        self._prepare_body(color)

    def get_segments(self):
        return self._segments

    def move_next(self):
        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        return self._segments[0]

    def grow_trail(self, number_of_segments, color):
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(color)
            self._segments.append(segment)

    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self,color):
        start = Point(random.randint(0,constants.MAX_X), random.randint(0,constants.MAX_Y)).scale(constants.CELL_SIZE)
        x = start.get_x()
        y = start.get_y()

        for i in range(constants.CYCLE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "O" if i == 0 else "#"
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)