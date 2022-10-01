import random

class Guess_word:
    '''A word to guess.
    The responsability is to randomly choose a word from a list,
    evaluate if a letter is contained in the word and check if the
    word has been guessed.
    Attributes:
        _word_2_guess(list): a word to guess in form of list
        masked_word(list): a list of the same lenght of word to guess, updated with guessed letters
    '''

    def __init__(self):
        '''Constructs a new Guess_word

        Args:
            self(Guess_word): an instance of Guess_word
        '''
        words = ['apple', 'banana', 'mango', 'strawberry','house', 'test']
        self._word_2_guess = list(random.choice(words))
        self.masked_word = []
        for _ in range(len(self._word_2_guess)):
            self.masked_word.append('_')
            
    
    def match_letter(self, letter_guess):
        '''Finds the if the letter guessed is in the word and retrieves the position.
        
        Args:
            self(Guess_word): an instance of Guess_word.

            letter_guess (char): the letter chose by the player.
        Return:
            found_position(list): list of letter recurrences position in the word.
        '''
        found_position = []
        index = 0 - len(letter_guess)
        try:
            while True:
                index = self._word_2_guess.index(letter_guess, index + len(letter_guess))
                found_position.append(index)
        except ValueError:
            pass
        return found_position

    def compare_words(self, word):
        '''Compares the word to guess with one provided.

        Args;
            self(Guess_word): an instance of Guess_word.

            word(list): a word in form of list, to compare.
        Return:
            winner (boolean): if words are equal winner is true.
        '''
        winner = False
        if self._word_2_guess == word:
            winner = True
        return winner
