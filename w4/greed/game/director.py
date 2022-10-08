from game.falling_obj import Falling_Object
from game.sprite import Sprite
from game.color import Color
from game.point import Point

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._score = 0
        
    def start_game(self, collection):
        """Starts the game using the given collection. Runs the main game loop.

        Args:
            collection (collection): The collection of sprites.
        """
        counter = 0
        self._video_service.open_window()
        self._set_gamer(collection)
        self._set_scorebanner(collection)
        while self._video_service.is_window_open():
            # count the number of cicles
            counter += 1
            # gap between the generation of stones
            if (counter % 30) == 0:
                self._set_stones(collection)
            # gap between the generation of diamonds
            if (counter % 30) == 0:
                self._set_diamonds(collection)
            self._get_inputs(collection)
            self._do_updates(collection)
            self._do_outputs(collection)
        self._video_service.close_window()

    def _set_scorebanner(self, collection):
        '''Sets the score banner at the top left of the screen.
        Args:
            collection (collection): The collection of sprites.
        '''
        score_banner = Sprite()
        score_banner.set_text("")
        score_banner.set_font_size(30)
        score_banner.set_color(Color(255, 255, 255))
        score_banner.set_position(Point(15, 0))
        collection.add_sprite("score_banners", score_banner)

    def _set_gamer(self, collection):
        '''Sets the gamer at the bottom of the screen.
        Args:
            collection (collection): The collection of sprites.
        '''
        x = int(900 / 2)
        y = 600 - 40
        position = Point(x, y)
        gamer = Sprite()
        gamer.set_text("#")
        gamer.set_font_size(30)
        gamer.set_color(Color(255, 255, 255))
        gamer.set_position(position)
        collection.add_sprite("gamers", gamer)

    def _set_stones(self, collection):
        '''Sets a new falling stone.
        Args:
            collection (collection): The collection of sprites.
        '''
        stone = Falling_Object()
        stone.set_text("o")
        stone.set_rndm_pos()
        stone.set_rndm_colr()
        collection.add_sprite("stones", stone)
    
    def _set_diamonds(self, collection):
        '''Sets a new falling diamond.
        Args:
            collection (collection): The collection of sprites.
        '''
        diamond = Falling_Object()
        diamond.set_text("*")
        diamond.set_rndm_pos()
        diamond.set_rndm_colr()
        collection.add_sprite("diamonds", diamond)

    def _get_inputs(self, collection):
        """Gets directional input from the keyboard and applies it to the gamer.
        
        Args:
            collection (collection): The collection of sprites.
        """
        gamer = collection.get_first_sprite("gamers")
        velocity = self._keyboard_service.get_direction()
        gamer.set_velocity(velocity.get_x(), velocity.get_y())
       

    def _do_updates(self, collection):
        """Updates the position of gamer, stones and diamonds.
        
        Args:
            collection (collection): The collection of sprites.
        """
        
        score_banner = collection.get_first_sprite("score_banners")
        gamer = collection.get_first_sprite("gamers")
        stones = collection.get_sprites("stones")
        diamonds = collection.get_sprites("diamonds")

        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        gamer.move_next(max_x, max_y)

        score_banner.set_text(f"Score: {self._score}")
        
        for stone in stones:
            stone.set_velocity(0,1)
            if gamer.get_position().equals(stone.get_position()):
                self._score -= 1
                collection.remove_sprite("stones", stone)
            stone.move_next(max_x, max_y)
        for diamond in diamonds:
            diamond.set_velocity(0,1)
            if  gamer.get_position().equals(diamond.get_position()):
                self._score += 1
                collection.remove_sprite("diamonds", diamond)
            diamond.move_next(max_x, max_y)

    def _do_outputs(self, collection):
        """Draws the sprites on the screen.
        
        Args:
            collection (collection): The collection of sprites.
        """
        self._video_service.clear_buffer()
        sprites = collection.get_all_sprites()
        self._video_service.draw_sprites(sprites)
        self._video_service.flush_buffer()