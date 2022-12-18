import random
from random import randint


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
        else:
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


def get_missile_coordinates(board_size):
    """
    This function takes the board_size,
    then asks user to input two values,
    values that need to be a number between 0 and board_size.
    """

    print(f"Please select the position of your missile whithin the board, by first choosing the row where this will land.\nNumbers need to be integers and within 0-{board_size-1} interval.")
    while True:
        missile_row = input()
        if (missile_row.isnumeric() and 0 <= int(missile_row) < board_size and 0 <= int(missile_row) < board_size):
            missile_row = int(missile_row)
            break
        else:
            print("Invalid number! Please try again.")

    print(f"Please select the position of your missile whithin the board by now choosing the column where this will land.\nNumbers need to be integers and within 1-{board_size-1} interval.")
    while True:
        missile_column = input()
        if (missile_column.isnumeric() and 0 <= int(missile_column) < board_size and 0 <= int(missile_column) < board_size):
            missile_column = int(missile_column)
            break
        else:
            print("Invalid number! Please try again.")
    return (missile_row, missile_column)


def check_sinking(missile_coordinates, ship_coordinates):
    """
    This function takes two tuples,
    missile_coordinates and ship_coordinates),
    compares them and then print a message
    accordingly
    """
    if missile_coordinates == ship_coordinates:
        print(f"Ship has been sinked!You won this battle!You have thrown missile at:{missile_coordinates} exactly were ship was located")
    else:
        print(f"You missed the ship!Missile was thrown at:{missile_coordinates} and ship was at:{ship_coordinates}")


def play_game():
    """
    Main function that gives the structure and the order,
    in which other functions are called.
    """
    display_instructions()
    board_size = get_board_size()
    board = display_board(board_size)
    ship_coordinates = get_random_ship(board_size)
    missile_coordinates = get_missile_coordinates(board_size)
    check_sinking(missile_coordinates, ship_coordinates)
    board = display_board(board_size, missile_coordinates, ship_coordinates)


if __name__ == "__main__":
    play_game()
