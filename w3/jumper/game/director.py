from game.terminal_IO import TerminalIO
from game.guess_word import Guess_word
from game.parachute import Parachute

class Director:
    '''A person who directs the game. 
    The responsibility of a Director is to control
    the sequence of play.
    Attributes:
        _game_won (boolean): if the player won.
        _game_lost (boolean): if the player lose.
        _is_playing (boolean): whether or not the game is being played.
        _error_counter (integer): counter of guess errors.
        _letter_guess (char): letter chose by player.
        _guessed_position (list): the positions in the word of the guessed letter.
    '''
    def __init__(self):
        '''Constructs a new Director

        Args:
            self(Director): an instance of Director
        '''
        pass
        self._game_won = False
        self._game_lost = False
        self._is_playing = True
        self._error_counter = 0
        self._term_IO = TerminalIO()
        self._word2guess = Guess_word()
        self._parrachute = Parachute()


    def start_game(self):
        '''Starts the game by running the main game loop.

        Args:
            self(Director): an instance of Director
        '''
        while self._is_playing:
            self._do_outputs()
            self._get_inputs()
            self._do_updates()
        self._do_outputs()
            
    
    def _get_inputs(self):
        '''Requires the player to guess a letter.

        Args:
            self(Director): an instance of Director
        '''
        self._letter_guess = self._term_IO.read_text('\nGuess a letter [a-z]: ')
        
    def _do_updates(self):
        '''Keeps the status of the game updated.
        Checks if the guessed letter is in the word 
        and updates the masked word, the parachute, 
        error counter, if the game is wor or lost.
        Args:
            self(Director): an instance of Director
        '''
        self._guessed_position = self._word2guess.match_letter(self._letter_guess)
        if len(self._guessed_position) != 0:
            for i in self._guessed_position:
                self._word2guess.masked_word[i] = self._letter_guess
        else:
            self._error_counter += 1
            self._parrachute.remove_line()
            if self._error_counter > 3:
                self._game_lost = True
                self._is_playing = False
        if self._word2guess.compare_words(self._word2guess.masked_word):
            self._game_won = True
            self._is_playing = False
        
    def _do_outputs(self):
        '''Displays the masked word, the parachute 
        and a message at the end of the game.
        Args:
            self(Director): an instance of Director
        '''
        self._term_IO.print_text(self._word2guess.masked_word)
        self._parrachute.draw_parachute()
        if self._game_won:
            self._term_IO.print_text('You won!!')
        if self._game_lost:
            self._term_IO.print_text('You lose!!')