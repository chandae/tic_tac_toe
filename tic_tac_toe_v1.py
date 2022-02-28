# Python Script for Tic Tac Toe by Chanda

info = """
    Tic-tac-toe, noughts and crosses, or Xs and Os is a paper-and-pencil game for two players who take turns marking
    the spaces in a three-by-three grid with X or O. The player who succeeds in placing three of their marks in a
    horizontal, vertical, or diagonal row is the winner. This Python script simulates this game.
"""

# initialise board
the_board = {}

def main():
    global the_board
    
    # print game info and instructions
    print(info)

    # Game Setup: Display initial state of board game
    print_board(board())

    # get player names
    print("\n To begin enter player names below: ")
    player_name_1 = input("Enter Player 1 name (X): ")
    player_name_2 = input("Enter Player 2 name (O): ")

    # initialise game marks X and O
    player_1 = 'X'
    player_2 = 'O'

    # Initialise variables
    turn = player_1

    # use for loop because the total numbers of moves is known
    for i in range(9):
        # check which player is making a move
        if turn == 'X':
            player_name = player_name_1
        else:
            player_name = player_name_2

        # within this function we check if the player has won
        game_done = player_move(turn, player_name)
        # check if there is victory
        if game_done:
            break
        # check whose turn it is
        if turn == player_1:
            turn = player_2
        else:
            turn = player_1

    # game finished message
    if not game_done:
        print("\n Game finished. Looks like a tie. Play with no strings attached if you want to win!")

# define board game
def board():
    global the_board

    # initialise a 3 X 3 grid structure
    the_board = {'1': ' ', '2': ' ', '3': ' ',
                 '4': ' ', '5': ' ', '6': ' ',
                 '7': ' ', '8': ' ', '9': ' '}
    return the_board

# Display board game
def print_board(game_board):

    # initialise a control guide for the game
    guide_board = {'1': '1', '2': '2', '3': '3',
                   '4': '4', '5': '5', '6': '6',
                   '7': '7', '8': '8', '9': '9'}

    print('\t\t' + 'Guide Board' + '')
    # Output guide board unto the screen
    print('\t\t' + guide_board['1'] + ' | ' + guide_board['2'] + ' | ' + guide_board['3'])
    print('\t\t' + '--+---+--')
    print('\t\t' + guide_board['4'] + ' | ' + guide_board['5'] + ' | ' + guide_board['6'])
    print('\t\t' + '--+---+--')
    print('\t\t' + guide_board['7'] + ' | ' + guide_board['8'] + ' | ' + guide_board['9'])

    # Output board unto the screen
    print('\n' + '\t\t' + 'Main Board' + '')
    print('\t\t' + game_board['1'] + ' | ' + game_board['2'] + ' | ' + game_board['3'])
    print('\t\t' + '--+---+--')
    print('\t\t' + game_board['4'] + ' | ' + game_board['5'] + ' | ' + game_board['6'])
    print('\t\t' + '--+---+--')
    print('\t\t' + game_board['7'] + ' | ' + game_board['8'] + ' | ' + game_board['9'])


# enter player moves on the board
def player_move(play, current_player):
    global the_board

    # get player move
    this_move = input(f"Your turn, {current_player}: ")

    # check if the move number is in the_board.keys
    if this_move in the_board.keys():
        # check if the selected slot is empty

        while the_board[this_move] != ' ':
            # qsk user/player to input another slot
            this_move = input(f"Try again slot is not empty, {current_player}: ")

        # insert the player move
        the_board[this_move] = play
        
        # check if there is victory
        if player_won(the_board, play):
            print_board(the_board)
            print(f"\n Congratulations! {current_player} won the game! Thanks for playing!")
            return True
        else:
            print_board(the_board)

# check if a player has won
def player_won(game_state, current_play):
    """Return True if player is a winner on this TTTBoard."""
    b, p = game_state, current_play  # Shorter names as "syntactic sugar".
    
    # Check for 3 marks across the 3 rows, 3 columns, and 2 diagonals.
    return ((b['1'] == b['2'] == b['3'] == p) or  # Across the top
            (b['4'] == b['5'] == b['6'] == p) or  # Across the middle
            (b['7'] == b['8'] == b['9'] == p) or  # Across the bottom
            (b['1'] == b['4'] == b['7'] == p) or  # Down the left
            (b['2'] == b['5'] == b['8'] == p) or  # Down the middle
            (b['3'] == b['6'] == b['9'] == p) or  # Down the right
            (b['3'] == b['5'] == b['7'] == p) or  # Diagonal
            (b['1'] == b['5'] == b['9'] == p))    # Diagonal


"""################################## Main ######################################"""

if __name__ == "__main__":
    # run tic tac toe
    main()
