class Parachute:
    '''
    The parachute drawing.
    The responsability is to draw and update the parachute.

    Attributes:
        _parachute(list): the picture of the parachute.
    '''
    def __init__(self):
        '''Constructs a new Parachute.
        
        Args:
            self(Parachute): an instance of Parachute
        '''
        self._parachute= ['  ___', ' /___\\', ' \\   /', '  \\ /', '   O', '  /|\\ ', '  / \\', '\n', '^^^^^^']
    
    def remove_line(self):
        '''Removes the first line from the parachute.
             
        Args:
            self(Parachute): an instance of Parachute   
        '''
        self._parachute.pop(0)
        self._check_parachute()

    def draw_parachute(self):
        '''Displays the parachute.
                
        Args:
            self(Parachute): an instance of Parachute
        '''
        for i in self._parachute:
            print (i)
    
    def _check_parachute(self):
        '''Checks if the parchute is gone and change the head of the jumper.
        
        Args:
            self(Parachute): an instance of Parachute
        '''
        if self._parachute[0] == '   O':
            self._parachute[0] = '   x'