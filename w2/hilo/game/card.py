import random

class Card:
    '''A playing card with value between 1 and 13.
    The responsibility of Card is to randomly generate a value to simulate drawing a card from a deck.
   
    Attributes:
        value (int): The number represented by the card.
    '''
    def __init__(self):
        '''Constructs a new instance of Card with a value attribute.

        Args:
            self (Card): An instance of Card.      
        '''
        self.value = 0
    
    def draw(self):
        '''Generates a new random value between 1 and 13.
        
        Args:
            self (Card): An instance of Card.      
        '''
        self.value = random.randint(1,13)
