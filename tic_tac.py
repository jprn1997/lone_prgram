# James P Norman
# cse210

#Set all of the varibles and set blank table.
turn = ()
X = 'X'
O = 'O'
BLANK = ' '
turn = X
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
black_board = {  
            "board": [
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK ]
        }

#Start the main function that runs the whole program. 
def main():
    #Display the blank table to start.
    display_board(board)
    #Compute wholes turn it is, I did it in here because I want to make it saveable.
    is_x_turn(board)
    #Start the game. 
    play_game(board,turn)
    #Display the final board. 
    display_board(board)
    return

#Function to display the board, uses the saved board and calls any used spot.
def display_board(board):
    # This sets the board so that we can call a specific spot in the board to swap it out.
    print(f" {board[0]} | {board[1]} | {board[2]}\n---+---+---\n {board[3]} | {board[4]} | {board[5]}\n ---+---+---\n {board[6]} | {board[7]} | {board[8]} \n")

#Function to determine whos turn it is. 
def is_x_turn(board):
    #Compare who has the most on the board and gives the turn to the next player, unles there is nothing on the board so is x turn.
    if board.count(X) < board.count(O):
        turn = X
    elif board.count(X) > board.count(O):
        turn = O
    else: 
        turn = X
    return turn

#Function that makes the game work.
def play_game(board, turn):
    #While
    while board.count(BLANK) > 0:
        game_done(board)
        turn = is_x_turn(board)
        print(f"it is {turn}s turn!")
        display_board(board)

        if game_done(board) == True:
            game_done(board,True)
            break
        elif turn == X:
            x_in = int(input("What is the space you would like to fill? "))                       
            board[x_in - 1] = turn
            
        elif turn == O:
            o_in = int(input("What is the space you would like to fill? "))
            board[o_in-1] = turn
        

    return False

#Function that computes who won.
def game_done(board, message=False):
    
    # Game is finished if someone has completed a row.
    for row in range(3):
        if board[row * 3] != BLANK and board[row * 3] == board[row * 3 + 1] == board[row * 3 + 2]:
            if message:
                print("The game was won by", board[row * 3])
            return True

    # Game is finished if someone has completed a column.
    for col in range(3):
        if board[col] != BLANK and board[col] == board[3 + col] == board[6 + col]:
            if message:
                print("The game was won by", board[col])


    # Game is finished if someone has a diagonal.
    if board[4] != BLANK and (board[0] == board[4] == board[8] or
                              board[2] == board[4] == board[6]):
        if message:
            print("The game was won by", board[4])
        return True
 
    # Game is finished if all the squares are filled.
    tie = True
    for square in board:
        if square == BLANK:
            tie = False
    if tie:
        if message:
            print("The game is a tie!")
        return True


    return False

#This displays the directions. 
print("Enter a number from 1 to 9")
print("where the following numbers are the locations on the grid:")
print(" 1 | 2 | 3 ")
print("---+---+---")
print(" 4 | 5 | 6 ")
print("---+---+---")
print(" 7 | 8 | 9 \n")
print("The current board is:")





if __name__ == "__main__":
    main()