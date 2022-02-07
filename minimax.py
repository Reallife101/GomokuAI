import math
import sys

# game stuff
BOARD = [['.']*15]*15

def getDia1Row(row: int, col: int):
    vert = []
    for i in range(-4, 5):
        if 0 <= row + i <= 14 and 0 <= col + i <= 14:
            vert.append(BOARD[row + i][col + i])
    return vert


def getDia2Row(row: int, col: int):
    vert = []
    for i in range(-4, 5):
        if 0 <= row + i <= 14 and 0 <= col + i <= 14:
            vert.append(BOARD[row + i][col + i])
    return vert

def getHorRow(row: int, col: int):
    vert = []
    for i in range(-4, 5):
        if 0 <= row + i <= 14:
            vert.append(BOARD[row + i][col])
    return vert

def getVertRow(row: int, col: int):
    vert = []
    for i in range(-4, 5):
        if 0 <= col + i <= 14:
            vert.append(BOARD[row][col + i])
    return vert

def checkRow(arr: [str], color):
    cont = 0
    for i in arr:
        if i == ('B' if color == 0 else 'W'):
            cont += 1
            if cont >= 5:
                return True
        else:
            cont = 0
    return False

def checkWin_helper(color: int, row: int, col: int):
    if checkRow(getVertRow(row, col), color) or checkRow(getHorRow(row, col), color) \
            or checkRow(getDia1Row(row, col), color) or checkRow(getDia2Row(row, col), color):
        print(f"{'Black' if color == 0 else 'White'} Wins!")
        return True
    return False

def checkWin():
    for row in range(15):
        for col in range(15):
            if BOARD[row][col] == 'B':
                if checkWin_helper(0, row, col):
                    return True
            elif BOARD[row][col] == 'W':
                if checkWin_helper(1, row, col):
                    return True
    return False

# minimax

max = sys.maxsize
min = -1*(sys.maxsize)

def minimax(depth, test_board, index, player, values, alpha, beta):
    # base case
    # if checkWin():
    #     return values[index]
    if depth == 3:
        return values[index]

    if player == 'max':
        pass
    # else:

# user interface

# prompts user for opponent move and returns row, col integers
def get_opponent():
    print("Enter opponents move")
    row = input("row: ")
    while not str.isdigit(row) or not (int(row) in range(15)):
        print("invalid row")
        row = input("row: ")
    col = input("column: ")
    while not str.isdigit(col) or not (int(col) in range(15)):
        print("invalid column")
        col = input("column: ")
    return row, col
us_char = 'W'
them_char = 'B'
first_second = input("Are you going first \"f\" or second \"s\"? ")
while first_second != 'f' or first_second != 's':
    print("enter \"f\" for first or \"s\" for second: ")
    first_second = input()
if first_second == 'f':
    us_char = 'B'
    them_char = 'W'
    print("Play row 7 column 7")
else:
    row, col = get_opponent()
    BOARD[row][col] = 'W'
turn = 'us'
if first_second == 'f':
    turn = 'them'
while not checkWin():
    if turn == 'us':
        row, col = minimax()
        print("Play row" + str(row) + ", col "+ str(col))
        BOARD[row][col] = us_char
        turn = 'them'
    else:
        row, col = get_opponent()
        BOARD[row][col] = them_char
        turn = 'us'