import string
import random
from pydantic import BaseModel


# Define tile pieces, their respective values and states
class Piece(BaseModel):
    active: bool
    guessed: bool = False
    character: str | None
    
    
class Player(BaseModel):
    name: str
    score: int


def extract_alphabet(alphabet_list: str, occurrence: int = -1):
    selected_alphabet = random.choice(alphabet_list)
    alphabet_list = alphabet_list.replace(
        selected_alphabet, "", occurrence
    )
    return alphabet_list, selected_alphabet


# Define the board
def Board(x: int, y: int):
    assert (
        x > 0 and y > 0 and x <= 9 and y <= 9
    ), f"The maximum size of the board is 9 x 9. Your input size is x:{x} y:{y}"
    assert x * y >= 3, f"Tiles have to be greater than 3. You have {x * y} tiles."

    quotient = x * y // 2

    alphabets_list = string.ascii_letters
    chosen_alphabets: string = ""

    for _ in range(quotient):
        alphabets_list, chosen_alphabet = extract_alphabet(alphabets_list)
        chosen_alphabets += chosen_alphabet

    chosen_alphabets += chosen_alphabets

    board = []

    for _ in range(x):
        row = []
        for _ in range(y):
            if chosen_alphabets != "":
                chosen_alphabets, selected_alphabet = extract_alphabet(
                    chosen_alphabets, 1
                )
                row.append(Piece(active=True, character=selected_alphabet))
            else:
                row.append(Piece(active=False, character=None))

        board.append(row)

    return board


def display(board):
    for row in board:
        print(*row, sep="\t")
        

def start():
    print("Determine the dimensions of board you want to play the game on.")
    x = input("x: ")
    x = int(x)
    y = input("y: ")
    y = int(y)

    endcount = x * y // 2

    board = Board(int(x), int(y))
    board_display = []

    for i in board:
        row = []
        for j in i:
            if j.active == True:
                row.append("?")
            else:
                row.append("@")
        board_display.append(row)

    display(board_display)

    while endcount != 0:
        print("Give the coordinate of the first value of a pair.")
        get_position_x1 = input("x1: ")
        get_position_y1 = input("y1: ")
        get_position_x1 = int(get_position_x1) - 1
        get_position_y1 = int(get_position_y1) - 1
        temp_value_1 = board[get_position_x1][get_position_y1]
        board_display[get_position_x1][get_position_y1] = temp_value_1.character
        display(board_display)
        print("Give the coordinate of the second value of a pair.")
        get_position_x2 = input("x2: ")
        get_position_y2 = input("y2: ")
        get_position_x2 = int(get_position_x2) - 1
        get_position_y2 = int(get_position_y2) - 1
        temp_value_2 = board[get_position_x2][get_position_y2]
        if (
            temp_value_1.character != temp_value_2.character
            or temp_value_1.guessed == True
            or temp_value_2.guessed == True
        ):
            if temp_value_1.guessed != True:
                board_display[get_position_x1][get_position_y1] = "?"
            print("Invalid value!")
        else:
            board_display[get_position_x2][get_position_y2] = temp_value_2.character
            board[get_position_x1][get_position_y1].guessed = True
            board[get_position_x2][get_position_y2].guessed = True
            endcount -= 1
        display(board_display)


start()
