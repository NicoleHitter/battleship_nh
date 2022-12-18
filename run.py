"""
Defines a series of functions for generating or manipulating random integers
"""
import random


def display_instructions():
    """
    This function is going to display:
    the welcome message and instructions for the player.
    """
    print("Welcome to Battleship-NH!\n")
    print("First you will be asked to introduce a number,")
    print("that will be the size of the board,")
    print("and then the row and column where you will throw the missile,")
    print("couting for these starts with 0.")
    print("Once this is done, you will be displayed a message")
    print("to confirm or not if you managed to hit the ship.")


def get_board_size():
    """
    Requests input from user,
    then input needs to be checkedif it is a number,
    and within the board size,
    if so this will be transformed into integer and returned.
    """
    print("Please choose the board size by entering a number between 4 and 9.")

    while True:
        board_size = input()
        if (board_size.isnumeric()) and (4 <= int(board_size) < 10):
            board_size = int(board_size)
            break
        print("Invalid number! Please try again.")

    return board_size


def display_board(board_size, missile_coordinates=None, ship_coordinates=None):
    """
    This function takes the board_size,
    then generates a board that has equal rows and columns to it,
    and places "M" and "S" at their specific coordinates,
    once these are declared
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


def get_random_ship(board_size):
    """
    This function will generate two random numbers,
    and then, return them as a tuple.
    """
    ship_row = random.randint(0, board_size-1)
    ship_column = random.randint(0, board_size-1)
    return (ship_row, ship_column)


def get_cell_value(board_size):
    """
    This functions asks user for an input,
    then checks if this is a number,
    and within the interval given,
    then returns it.
    """
    while True:
        cell_location = input()
        if (cell_location.isnumeric() and
            0 <= int(cell_location) < board_size and
            0 <= int(cell_location) < board_size):
            return int(cell_location)
        print("Invalid number! Please try again.")


def get_missile_coordinates(board_size):
    """
    This function takes the board_size,
    then asks user to input two values,
    values that need to be a number between 0 and board_size.
    """

    print("Please select the position of your missile whithin the board,")
    print("by first choosing the row where this will land.")
    print(f"Numbers need to be integers and within 0-{board_size-1} interval.")
    missile_row = get_cell_value(board_size)

    print("Now chose the column where this will land.")
    print(f"Numbers need to be integers and within 0-{board_size-1} interval.")
    missile_column = get_cell_value(board_size)
    return (missile_row, missile_column)


def check_sinking(missile_coordinates, ship_coordinates):
    """
    This function takes two tuples,
    missile_coordinates and ship_coordinates),
    compares them and then print a message
    accordingly
    """
    if missile_coordinates == ship_coordinates:
        print("Ship has been sinked!You won this battle!")
        print(f"You have thrown missile at:{missile_coordinates} exactly were ship was located")
    else:
        print("You missed the ship!")
        print(f"Missile was thrown at:{missile_coordinates} and ship was at:{ship_coordinates}")


def play_game():
    """
    Main function that gives the structure and the order,
    in which other functions are called.
    """
    display_instructions()
    board_size = get_board_size()
    display_board(board_size)
    ship_coordinates = get_random_ship(board_size)
    missile_coordinates = get_missile_coordinates(board_size)
    check_sinking(missile_coordinates, ship_coordinates)
    display_board(board_size, missile_coordinates, ship_coordinates)


if __name__ == "__main__":
    play_game()
