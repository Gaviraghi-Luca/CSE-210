#CSE 210
#W01 Prove: Developer
#Author: Luca Gaviraghi


def main():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    possible_choices_list = [1,2,3,4,5,6,7,8,9]
    game_won = 0
    max_choices = 9
    choice_counter = 0
    player = int(input(f'Choose the player to start playing (press \'0\' or \'1\'): '))
    while choice_counter < max_choices and game_won == 0:
        grid_print(matrix)
        choose_position = player_position_choice(possible_choices_list, player)
        if choose_position != 999999:
            choice_counter += 1
            matrix = grid_position(matrix, choose_position, player)
            game_won = game_status_check(matrix)
            player = player_turn(player)
        else:
            print('\nSquare chosen is not correct. Select a valid one!!')
    grid_print(matrix)
    if game_won == 0:
        print('\nNobody wins. Game draw!\n')


def player_position_choice(possible_choices_list, player):
    '''The function requires the player to enter the choiced square and validates the input.

    Parameter:

        possible_choices_list, the list of squares the player can choose.

        player, the id of the player.
    
    Returns:

        the value selected or 999999 in case of invalid selection.
    '''
    player_choice = input(f'Player {player} turn to choose a valid square ({possible_choices_list}): ')
    for i in range(len(possible_choices_list)):
        if possible_choices_list[i] == int(player_choice):
            possible_choices_list.pop(i)
            return player_choice
        else:
            return 999999


def game_status_check(matrix):
    '''The function checks rows, colums and diagonals to evalauate if a player wins. And prints a message if found a winner.

    Parameter:

        matrix, A 3x3 matrix of integers.
    
    Returns:

        0 (none has won) or 1 (a player has won).   
    '''
    #rows status check. If the sum of a row is 0 or -3 
    for i in range(3):
        row_count = 0
        for j in range(3):
            row_count += matrix[i][j]
        if row_count == 0:
            print ('\nPlayer 0 wins!\n')
            return 1
        elif row_count == -3:
            print ('\nPlayer 1 wins!\n')
            return 1
    #columns status check
    for j in range(3):
        col_count = 0
        for i in range(3):
            col_count += matrix[i][j]
        if col_count == 0:
            print ('\nPlayer 0 wins!\n')
            return 1
        elif col_count == -3:
            print ('\nPlayer 1 wins!\n')
            return 1
    #first diagonal status check
    first_dgn_count = 0
    for i in range(3):
        first_dgn_count += matrix[i][i]
    if first_dgn_count == 0:
        print ('\nPlayer 0 wins!\n')
        return 1
    elif first_dgn_count == -3:
        print ('\nPlayer 1 wins!\n')
        return 1
    #second diagonal status check
    second_dgn_count = 0
    for i in range(3):
        second_dgn_count += matrix[i][2-i]
    if second_dgn_count == 0:
        print ('\nPlayer 0 wins!\n')
        return 1
    elif second_dgn_count == -3:
        print ('\nPlayer 1 wins!\n')
        return 1
    #return 0 if none has won
    return 0


def player_turn (player):
    '''The function alternates the players.
    
    Parameter:
        player, the player playing identifed by an integer 0 or 1
    
    Returns:
        player, the next player, identifed by an integer 0 or 1
    '''
    player += 1
    return player % 2


def grid_position(matrix, choice, player):
    '''The function change the selected element of a matrix to 0 or -1 according to the player playing.
    
    Parameter:
        matrix, a 3x3 matrix of integers.

        choice, the square choiced by the player.

        player, the player playing.

    Returns:
        matrix, the updated matrix
    '''
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == int(choice):
                if player == 0:
                    matrix[i][j] = 0
                elif player == 1:
                    matrix[i][j] = -1
    return matrix


def grid_print(matrix):
    '''The function prints a matrix for tic-tac-toe.

    Parameter:
        matrix, a 3x3 matrix of integers.
    
    Returns:
        None
    '''
    print('\n+-++-++-+')
    for i in matrix:
        for j in i:
            if j == 0:
                j = 'O'
            if j == -1:
                j = 'X'
            print(f'|{j}', end='|')
        print('')
        print('+-++-++-+')
    print()


if __name__ == '__main__':
    main()