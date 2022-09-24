from game.card import Card

class Dealer:
    '''A person who directs the game. 
    The responsibility of a Dealer is to control the sequence of play.

        Attributes:
            curr_card (int): The value of the current card.
            next_card (int): the value of the next card.
            guess_card (string): The guess of the player.
            score (int): The score for the game.
            is_playing (boolean): Whether or not the game is being played.  
    '''


    def __init__(self):
        '''Constructs a new Dealer.
        
        Args:
            self (Dealer): an instance of Dealer
        '''
        card = Card()
        card.draw()
        self.curr_card = card.value
        self.is_playing = True
        self.score = 300
    

    def start_game(self):
        '''Starts the game by running the main game loop.
        
        Args:
            self (Dealer): an instance of Dealer. 
        '''
        while self.is_playing:
            self.get_input()
            self.do_updates()
            self.do_output()


    def get_input(self):
        '''Shows the user the current card and asks to guess if the next one will be higher or lower.

        Args:
            self (Dealer): An instance of Dealer.
        
        '''
        print(f'\nThe card is: {self.curr_card}')
        self.guess_card = input(f'Higher or lower? [h/l] ')
 

    def do_output(self):
        '''Displays the score, and if score is higher than 0 asks if the player wants to play again. 

        Args:
            self (Dealer): An instance of Dealer. 
        '''
        print(f'You score is: {self.score}')
        if self.score > 0:
            play_again = input(f'Play again? [y/n] ')
            self.is_playing = (play_again.lower() == "y")
        else:
            self.is_playing = False


    def do_updates(self):
        '''Generates the next card.
        Check if the user guessed corrctly and update the score.
        Updates the current card value.
        
        Args:
            self (Dealer): An instance of Dealer.      
        '''
        card = Card()
        card.draw()
        self.next_card = card.value
        print(f'Next card is: {self.next_card}')
        if ((self.guess_card.lower() == 'h') and (self.next_card > self.curr_card)) or ((self.guess_card.lower() == 'l') and (self.next_card < self.curr_card)):
            self.score += 100
        else:
            self.score -= 75
        self.curr_card = self.next_card