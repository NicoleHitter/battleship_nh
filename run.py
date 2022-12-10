from random import randint

board = []
"""
Welcome message 
"""
print("Welcome to Battleship!")

"""
Request user to select number of rows and columns
"""
while True:
    try:
        board_size = int(input("Please enter the number of rows and columns (4-9).\n"))
    except ValueError:
        print("Not a number! Please try again!")
    else:
        if 4 <= board_size < 10:
            break
        else:
            print("Invalid number! Please try again.")


def create_board(board_size):
    """
    Creates the board using the board_size number 
    """
    for x in range(board_size):
        row = []
        for y in range(board_size):
            row.append(".")
        board.append(row)
    return board


def display_board(board, board_size):
    """
    Iterating through list elements and displaying them 
    in rows of the board_size length
    """
    for x in range(board_size):
        for y in range(0,board_size,board_size):
            print(board[x][y]*board_size)
   

create_board(board_size)
display_board(board,board_size)

