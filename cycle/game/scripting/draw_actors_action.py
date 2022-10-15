from game.scripting.action import Action


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        self._video_service.clear_buffer()
        scores =cast.get_actors("scores")
        cycles = cast.get_actors("cycles")
        for cycle in cycles:
            segments = cycle.get_segments()
            self._video_service.draw_actors(segments)
        
        # show scores Player1 at left and Player2 at right
        self._video_service.draw_actor(scores[0],0,0)
        self._video_service.draw_actor(scores[1],0,1)

        messages = cast.get_actors("messages")
        self._video_service.draw_actors(messages)
        self._video_service.flush_buffer()