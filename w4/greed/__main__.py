from game.sprite_collection import Sprite_Collection
from game.director import Director
from game.keyboard_service import KeyboardService
from game.video_service import VideoService


FRAME_RATE = 10
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 30
FONT_SIZE = 30
COLS = 30
ROWS = 20
CAPTION = "Greed"


def main():
    # create the collection of sprites
    collection = Sprite_Collection()
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(collection)


if __name__ == "__main__":
    main()