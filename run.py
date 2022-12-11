import random
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
    that will be the player's guessed coordinates  
    for the ship
    which before beeing passed to new_board 
    will need to be validated 
    """
    print(f"Please select the position of your ship whithin the board by choosing the column and row where this is located.\nNumbers need to be integers and within 1-{board_size} interval.")
    while True:
        try:
            r = int(input())
            c = int(input())

        except ValueError:
            print("Not a number! Please try again!")
        else:
            if 1 <= c < board_size and 1<= r <board_size:
                break
            else:
                print("Invalid number! Please try again.")

    new_board = board
    new_board[r-1][c-1] = "@"
    return new_board

def random_ship():
    """
    This function will generate two random numbers 
    that will be the real ship coordinates
    """
    r_rand = random.randint(1,board_size)
    c_rand = random.randint(1,board_size)
    
    print(r_rand,c_rand) 


create_board(board_size)
display_board(board,board_size)
new_board = get_ship_coordinates(board,c,r)
display_board(new_board,board_size)
random_ship()






