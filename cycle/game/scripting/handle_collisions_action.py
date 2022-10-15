import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point
from game.scripting.avoid_collision_action import AvoidCollisionAction
from game.scripting.control_actors_action import ControlActorsAction
from game.services.keyboard_service import KeyboardService

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the cycle collides
    with the food, or the cycle collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_segment_collision(cast)
            self._handle_game_over(cast, script)

    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the cycle collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        cycles = cast.get_actors('cycles')
        scores = cast.get_actors('scores')
        cycle_1_head = cycles[0].get_segments()[0]
        cycle_1_body = cycles[0].get_segments()[1:]
        cycle_2_head = cycles[1].get_segments()[0]
        cycle_2_body = cycles[1].get_segments()[1:]
        for segment in cycle_1_body:
            if cycle_2_head.get_position().equals(segment.get_position()):
                self._is_game_over = True
                scores[0].add_points(1)
        for segment in cycle_2_body:
            if cycle_1_head.get_position().equals(segment.get_position()):
                self._is_game_over = True
                scores[1].add_points(1)
        
    def _handle_game_over(self, cast, script):
        """Shows the 'game over' message and turns the cycle and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            cycles = cast.get_actors('cycles')
            for cycle in cycles:
                segments = cycle.get_segments()
                for segment in segments:
                    segment.set_color(constants.WHITE)

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("!! Game Over !!")
            message.set_position(position)
            cast.add_actor("messages", message)
            # Add AvoidCollisionAction to script
            script.add_action("update", AvoidCollisionAction())
            # Remove GrowTrailAction from script
            actions = script.get_actions("update")
            script.remove_action("update", actions[0])