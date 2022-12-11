import random
from random import randint

board = []
b=[]
new_board = []
c = 0
r = 0
r_rand = 0
c_rand = 0
s_coordinates = []
m_coordinates = []

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
        
   
def get_missile_coordinates(board,r,c):
    """
    Request user to give two numbers
    that will be the player's guessed coordinates  
    for the ship
    which before beeing passed to new_board 
    will need to be validated 
    """
    print(f"Please select the position of your missile whithin the board by choosing the column and row where this will land.\nNumbers need to be integers and within 1-{board_size} interval.")
    while True:
        try:
            r = int(input())
            c = int(input())

        except ValueError:
            print("Not a number! Please try again!")
        else:
            if 1 <= c < board_size and 1<= r < board_size:
                break
            else:
                print("Invalid number! Please try again.")
    global m_coordinates 
    m_coordinates.append(r)
    m_coordinates.append(c)

    new_board = board
    new_board[r-1][c-1] = "@"
    return new_board 

def random_ship():
    """
    This function will generate two random numbers 
    that will be the real ship coordinates
    """
    global r_rand
    global c_rand 
    global s_coordinates 

    r_rand = random.randint(1,board_size)
    c_rand = random.randint(1,board_size)
    
    s_coordinates.append(r_rand)
    s_coordinates.append(c_rand)
    return s_coordinates
    

def check_sinking(m_coordinates, s_coordinates):
    """
    This function checks if ship has been hit 
    by checking if the coordinates of the ship
    are the same coordinates with the missile
    """
    if m_coordinates == s_coordinates:
        print(f"Ship has been sinked!You won this battle!You have thrown missile at:{s_coordinates} exactly were ship was located")
    else:
        print(f"You missed the ship!Missile was thrown at:{m_coordinates} and ship was at:{s_coordinates}")

        

create_board(board_size)
display_board(board,board_size)
new_board = get_missile_coordinates(board,c,r)
display_board(new_board,board_size)
s_coordinates = random_ship()
print(r_rand)
print(c_rand)
check_sinking(m_coordinates, s_coordinates)







