class Director:
    """
    A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _video_service (VideoPhysicsService): For providing video output.
        _physics_service (PhysicsService): For providing physics emulation.
    """

    def __init__(self, video_service, physics_service):
        """
        Constructs a new Director using the specified video and physics services.
        
        Args:
            video_service (VideoPhysicsService): An instance of VideoPhysicsService.
            physics_service (PhysicsService): An instance of PhysicsService.
        """
        self._video_service = video_service
        self._physics_service = physics_service
        
    def start_game(self):
        """
        Starts the game. Runs the main game loop.
        """
        self._video_service.open_window()
        self._physics_service.create_player()
        while self._video_service.is_window_open():
            self._update_game()
        self._video_service.close_window()

    def _update_game(self):
        """
            Update the game
        """
        self._physics_service.update()
        self._video_service.clear_buffer()
        self._video_service.print_message("Press space bar to add a new object. Close the window to end the game.", 1)
        self._video_service.print_message("Player is the red object. Use arrow keys to move the player", 2)
        bc = self._physics_service.get_bodies_count()
        self._video_service.print_message("There are " +str(bc) +" bodies", 3)
        self._physics_service.create_things()
        # body with index 1 is the player to move
        self._physics_service.move_thing(1)
        for i in range(bc):
            self._video_service.draw_body(i)
            # destroy bodies outside the screen
            self._physics_service.destroy_external_body(i)
        self._video_service.flush_buffer()
         