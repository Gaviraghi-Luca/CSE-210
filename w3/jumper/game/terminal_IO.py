import string

class TerminalIO:
    '''A service that handles terminal I/O.
    
    The responsibility of a TerminalIO is 
    to provide input and output operations for the 
    terminal.
    '''
     
    def read_text(self, prompt):
        '''Gets text input from the terminal.
        Validates input.

        Args: 
            self (TerminalIO): An instance of TerminalIO.
            prompt (string): The prompt to display on the terminal.

        Returns:
            string: The user's input as text.
        '''
        letters = list(string.ascii_letters)
        request_loop = True
        while request_loop:
            text_input = input(prompt)
            if text_input in letters:
                return text_input.lower()
            else:
                print('You did not enter a letter.') 
        
    def print_text(self, draw):
        '''Displays the given text on the terminal. 

        Args: 
            self (TerminalIO): An instance of TerminalIO.
            draw (list): The text to display.
        '''
        print('\n')
        for i in draw:
            print(i, end=' ')
        print('\n')