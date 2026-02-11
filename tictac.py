from random import randrange

board = [['1', '2', '3'],
         ['4', 'X', '6'],
         ['7', '8', '9']]


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    for row in board:
        print('+-------' * 3 + '+')
        print('|       ' * 3 + '|')
        print('|   ' + '   |   '.join(row) + '   |')
        print('|       ' * 3 + '|')
    print('+-------' * 3 + '+') 
    

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    while True:
        try:
            user_input = int(input("Enter your move : "))
            if user_input < 1 or user_input > 9:
                print("Invalid input. Please enter a number from 1 to 9.")
                continue
            row = (user_input - 1) // 3
            col = (user_input - 1) % 3
            if board[row][col] in ['O', 'X']:
                print("Cell already taken. Please try again.")
                continue
            board[row][col] = 'O'
            break
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 9.")
        except Exception as e:
            print(f"Error: {e}")


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_squares = []
    for r in range(3):
        for c in range(3):
            if board[r][c] not in ['O', 'X']:
                free_squares.append((r, c))
    return free_squares

    


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    for r in range(3):
        if all(board[r][c] == sign for c in range(3)):
            return True
    for c in range(3):
        if all(board[r][c] == sign for r in range(3)):
            return True
    if all(board[i][i] == sign for i in range(3)):
        return True
    if all(board[i][2-i] == sign for i in range(3)):
        return True
    return False

def draw_move(board):
    # The function draws the computer's move and updates the board.
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        r, c = free_fields[randrange(len(free_fields))]
        board[r][c] = 'X'

if __name__ == "__main__":
    while True:
        display_board(board)
        enter_move(board)
        if victory_for(board, 'O'):
            print("Congratulations! You win!")
            break
        draw_move(board)
        if victory_for(board, 'X'):
            print("Computer wins! Better luck next time.")
            break
        if not make_list_of_free_fields(board):
            print("It's a draw!")
            break