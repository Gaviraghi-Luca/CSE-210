import pyray as pr
import constants

class VideoService:
    """
    Outputs the game state. The responsibility of the class of objects is to draw the game state 
    on the screen. 
    """

    def __init__(self):
        """
        Constructs a new VideoService.
        """
        pass

    def close_window(self):
        """
        Closes the window and releases all computing resources.
        """
        pr.close_physics()
        pr.close_window()

    def clear_buffer(self):
        """
        Clears the buffer in preparation for the next rendering. This method should be called at
        the beginning of the game's output phase.
        """
        pr.begin_drawing()
        pr.clear_background(pr.BLACK)
    
    def flush_buffer(self):
        """
        Copies the buffer contents to the screen. This method should be called at the end of
        the game's output phase.
        """ 
        pr.end_drawing()

    def is_window_open(self):
        """
        Whether or not the window was closed by the user.

        Returns:
            bool: True if the window is closing; false if otherwise.
        """
        return not pr.window_should_close()

    def open_window(self):
        """
        Opens a new window with the provided title.

        Args:
            title (string): The title of the window.
        """
        pr.init_window(constants.MAX_X, constants.MAX_Y, constants.CAPTION)
        pr.set_target_fps(constants.FRAME_RATE)

    def print_message(self, message, row):
        """
        Prints message on screen.
        
        Args:
            message (str): message to display.
            row (int): row number.
        """
        pr.draw_text(message, 10, row * 20, 20, pr.WHITE)

