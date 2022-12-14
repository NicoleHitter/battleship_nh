import random
from random import randint


def display_instructions():
    """
    This functions is going to display 
    welcome messafe and instructions 
    for the player
    """
    print("Welcome to Battleship-NH!\n")
    print("First you will be asked to introduce a number,")
    print("that will be the size of the board,")
    print("and then the row and column where you will throw the missile.")
    print("Once this is done, you will be displayed message")
    print("to confirm or not if you managed to hit the ship.")


def get_board_size():
    """
    Request user to select a number 
    that will give the size of the board
    """
    print("Please enter a number between 4 and 9.")

    while True:
        board_size = input()
        if (board_size.isnumeric()) and (4 <= int(board_size) < 10):
            board_size = int(board_size)
            break
        
        else:
            print("Invalid number! Please try again.")
            
        
    return board_size


def display_board(board_size, missile_coordinates=None, ship_coordinates=None):
    """
    Iterating through list elements and displaying them 
    in rows of the board_size length
    """
    
    for row in range(board_size):
        for column in range(board_size):
            board_coordinates = (row, column)
            if board_coordinates == missile_coordinates:
                print("M ", end=' ')
            elif board_coordinates == ship_coordinates:
                print("S ", end=' ')
            else:
                print(". ", end=' ')
        print("\n")
        
   
def get_missile_coordinates(board_size):
    """
    Request user to give two numbers
    that will be the player's guessed coordinates  
    for the ship
    which before beeing passed to new_board 
    will need to be validated 
    """
    print(f"Please select the position of your missile whithin the board by first choosing the row where this will land.\nNumbers need to be integers and within 1-{board_size} interval.")
    while True:
        missile_row = input()
        if (missile_row.isnumeric() and 1 <= int(missile_row) < board_size and 1<= int(missile_row) < board_size):
            missile_row = int(missile_row)
            break
        else:
            print("Invalid number! Please try again.")

    print(f"Please select the position of your missile whithin the board by first choosing the column where this will land.\nNumbers need to be integers and within 1-{board_size} interval.")
    while True:
        missile_column = input()
        if (missile_column.isnumeric() and 1 <= int(missile_column) < board_size and 1<= int(missile_column) < board_size):
            missile_column = int(missile_column)
            break
        else:
            print("Invalid number! Please try again.")         
  
    return (missile_row, missile_column)


def get_random_ship():
    """
    This function will generate two random numbers 
    that will be the real ship coordinates
    """
    ship_row = random.randint(1,board_size)
    ship_column = random.randint(1,board_size)
    
    return (ship_row, ship_column)
    

def check_sinking(missile_coordinates, ship_coordinates):
    """
    This function checks if ship has been hit 
    by checking if the coordinates of the ship
    are the same coordinates with the missile
    """
    if missile_coordinates == ship_coordinates:
        print(f"Ship has been sinked!You won this battle!You have thrown missile at:{missile_coordinates} exactly were ship was located")
    else:
        print(f"You missed the ship!Missile was thrown at:{missile_coordinates} and ship was at:{ship_coordinates}")


def play_game():
    """
    Main function that gives the structure 
    and the order in which other functions 
    are called.
    """
    display_instructions()
    board_size = get_board_size()
    board = display_board(board_size)
    missile_coordinates = get_missile_coordinates()
    print(missile_coordinates)
    ship_coordinates = get_random_ship()
    print(ship_coordinates)
    check_sinking(missile_coordinates, ship_coordinates)
    board = display_board(board_size, missile_coordinates, ship_coordinates)



missile_coordinates = get_missile_coordinates(5)
print(missile_coordinates)