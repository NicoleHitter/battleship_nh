from random import randint

board = []
b=[]
new_board = []
c=0
r=0
"""
Welcome message 
"""
print("Welcome to Battleship!")

"""
Request user to select a number 
that will give the number of rows and columns 
for the board 
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


def display_board(b, board_size):
    """
    Iterating through list elements and displaying them 
    in rows of the board_size length
    """
    elements = []
    for x in range(board_size):
        for y in range(board_size):
            elements.append(b[x][y])
    
    for i in range(0,len(elements),board_size):
        print(*elements[i:i+board_size])
        
   
def get_ship_coordinates(board,c,r):
    """
    Request user to give two numbers
    that will be the ship coordinates  
    """
    print("Please select the position of your ship whithin the board by choosing the column and row where this is located.")
    c = int(input())
    r = int(input())
    new_board = board
    new_board[c-1][r-1] = "@"
    return new_board


create_board(board_size)
display_board(board,board_size)
new_board = get_ship_coordinates(board,c,r)
display_board(new_board,board_size)







