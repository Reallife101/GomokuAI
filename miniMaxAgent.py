from typing import List
from Gomoku import *

def getHorizontals(board, player):
    # * for piece placed, b for blocked square, o for open square
    horizontals = ['' for i in range(15)]
    for i in range(15):
        for j in range(15):
            if board[i][j] == 3 - player:   # your pieces
                horizontals[i] += '*'
            elif board[i][j] == 0:          # empty space
                horizontals[i] += 'o'
            elif board[i][j] == player:     # other person's space
                horizontals[i] += 'b'
    return horizontals


def getVerticals(board, player):
    # * for piece placed, b for blocked square, o for open square
    verticals = ['' for i in range(15)]
    for i in range(15):
        for j in range(15):
            if board[i][j] == 3 - player:
                verticals[j] += 'b'
            elif board[i][j] == 0:
                verticals[j] += 'o'
            elif board[i][j] == player:
                verticals[j] += '*'
    return verticals


def getLeftDiags(board, player):
    diags = ['' for i in range(21)]
    for i in range(15):
        if board[i][i] == 3 - player:  
            diags[0] += 'x'
        elif board[i][i] == 0:         # empty space
            diags[0] += 'o'
        elif board[i][i] == player:
            diags[0] += '*'
    for i in range(10):
        for j in range(15):
            if (i + 1 + j) > 14 or board[i + 1 + j][j] == 3 - player:
                diags[i + 1] += 'x'
            elif board[i + 1 + j][j] == 0:
                diags[i + 1] += 'o'
            elif board[i + 1 + j][j] == player:
                diags[i + 1] += '*'
    for i in range(10):
        for j in range(15):
            if (i + 1 + j) > 14 or board[j][i + 1 + j] == 3 - player:
                diags[i + 11] += 'x'
            elif board[j][i + 1 + j] == 0:
                diags[i + 11] += 'o'
            elif board[j][i + 1 + j] == player:
                diags[i + 11] += '*'

    return diags


def getRightDiags(board, player):
    diags = ['' for i in range(21)]
    for i in range(15):
        if board[i][14 - i] == 3 - player:
            diags[0] += 'x'
        elif board[i][18 - i] == 0:
            diags[0] += 'o'
        elif board[i][18 - i] == player:
            diags[0] += '*'
    for i in range(10):
        for j in range(15):
            if (10 - i + j) > 14 or board[10 - i + j][14 - j] == 3 - player:
                diags[i + 1] += 'x'
            elif board[10 - i + j][14 - j] == 0:
                diags[i + 1] += 'o'
            elif board[10 - i + j][14 - j] == player:
                diags[i + 1] += '*'
    for i in range(10):
        for j in range(15):
            if (13 - j) - i < 0 or board[j][(13 - j) - i] == 3 - player:
                diags[i + 11] += 'x'
            elif board[j][(13 - j) - i] == 0:
                diags[i + 11] += 'o'
            elif board[j][(13 - j) - i] == player:
                diags[i + 11] += '*'

    return diags


def eval(board, player):
    newBoard = board.copy()
    hori = getHorizontals(newBoard, player)
    vert = getVerticals(newBoard, player)
    leftD = getLeftDiags(newBoard, player)
    rightD = getRightDiags(newBoard, player)
    allLines = hori + vert + leftD + rightD
    allLines = [line for line in allLines if line.count('*') > 1]

    score = 0

    for line in allLines:
        score += evalLine(line)
    return score


def evalLine(line):
    # * for piece placed, x for blocked square, o for open square

    five = '*****'

    open_four = 'o****o'

    closed_four1 = 'x****o'
    closed_four2 = 'o****x'
    closed_four3 = '*o***'
    closed_four4 = '***o*'
    closed_four5 = '**o**'

    open_three1 = 'o***oo'
    open_three2 = 'oo***o'
    open_three3 = 'o*o**o'
    open_three4 = 'o**o*o'

    closed_three1 = 'x***oo'
    closed_three2 = 'oo***x'
    closed_three3 = 'xo***ox'
    closed_three4 = 'o*o**x'
    closed_three5 = 'x*o**o'
    closed_three6 = 'x**o*o'
    closed_three6 = 'o**o*x'

    open_two1 = 'o**o'
    open_two2 = 'o*o*o'
    open_two3 = 'o*oo*o'

    closed_two1 = 'x**o'
    closed_two2 = 'x*o*o'
    closed_two3 = 'o*o*x'
    closed_two4 = 'o**x'

    five_count = line.count(five)
    four_count = line.count(open_four)
    cfour_count = line.count(closed_four1) + line.count(closed_four2) + line.count(closed_four3) + line.count(
        closed_four4) + line.count(closed_four5)
    three_count = line.count(open_three1) + line.count(open_three2) + line.count(open_three3) + line.count(open_three4)
    cthree_count = line.count(closed_three1) + line.count(closed_three2) + line.count(closed_three3) + line.count(
        closed_three4) + line.count(closed_three5) + line.count(closed_three6)
    two_count = line.count(open_two1) + line.count(open_two2) + line.count(open_two3)
    ctwo_count = line.count(closed_two1) + line.count(closed_two2) + line.count(closed_two3) + line.count(closed_two4)

    if five_count:
        return 1000000
    if four_count:
        return 99999
    if cfour_count + three_count > 1:
        return 9000
    score = 200 * (cfour_count + three_count) + 10 * (cthree_count + two_count) + 5 * (ctwo_count)

    return score


def getMoves(board):
    moves = []
    for i in range(15):
        for j in range(15):
            if board[i][j] == 0:
                score = 7 - max(abs(i - 7), abs(j - 7))
                moves.append((score, i, j))
    moves.sort()
    moves.reverse()
    return moves


def checkWinner(board, player):
    directions = ((1, 0), (0, 1), (1, 1), (1, -1))
    for i in range(15):
        for j in range(15):
            if board[i][j] != player:
                continue
            for dir in directions:
                c, r = i, j
                count = 0
                for k in range(5):
                    if c > 14 or c < 0 or r > 14 or r < 0 or board[c][r] != player:
                        break
                    c += dir[0]
                    r += dir[1]
                    count += 1
                if count == 5:
                    return True
    return False


    #possibly change checkRow to take in an int
    #5 for win already done
    #4 will be found in groups of 3s, but need to do for need to block in open state
    #3 for needed block on either side
    #2 for check if two 2s collide with each other
        #check if 
    #make a copy of the file or go into a new branch



'''
def placePiece(arr: [str], space: int, color: int, num: int):
    if arr[space + 1] == "o":   
            arr[space + 1] = "*" # do we just say where we want the next token or actually place it  would need to say what color the piece is
                                 # need to update the actual board and end turn 
    elif arr[space + 1] in  "x*":
        if arr[space - num] == "o":  
            arr[space - num] = "*"    #num is 4 in check4
'''

##########################################
##           make columns rows          ##
##########################################
def make_column_row(legit_puzzle, j):
    column = []
    for row in legit_puzzle:
        column.append(row[j])
    string_column = ''.join(column)
    return string_column


def make_invert(legit_puzzle):          #this is making colums rows
   invert = []
   for j in range(0,15):
      column = make_column_row(legit_puzzle, j)
      invert.append(column)
   return invert


def check_forward(legit_puzzle, word):
    row_num = 0
    while row_num <= 14:
        if legit_puzzle[row_num].find(word) != -1:
            col_num = legit_puzzle[row_num].find(word)
            return (row_num, col_num)
        row_num += 1


def check_down(invert, word):
    col_num = 0
    while col_num <= 9:
        if invert[col_num].find(word) != -1:
            row_num = invert[col_num].find(word)
            #return word + ": (UP) row: " + str(row_num) + " column: " + str(col_num)
            return (row_num, col_num)
        col_num += 1
    #else:
        #pass


def check_diagonal(legit_puzzle, word):
    row_num = 0
    col_num = 0
    index = 0
    #have a value to store the first letter of the word when found
    #for loop from row 0-9, then another from col 0-9
    while row_num <= 9:
        if legit_puzzle[row_num + index][col_num + index] == word[index]:
            index += 1
            if len(word) == index:
                return (row_num, col_num)
            elif col_num >= 14: #this is just to catch row_num and col_num, nothing to do with indicies
                col_num = 0
                row_num += 1
                if row_num + index > 14:
                    index = 0
                    col_num += 1
            elif row_num + index > 14:
                index = 0 #check to make sure the index resets to 0
                col_num += 1
                if col_num > 14:
                    col_num = 0
                    row_num += 1
            elif col_num + index > 14:
                index = 0 #check to make sure the index resets to 0
                col_num += 1
                if col_num > 14:
                    col_num = 0
                    row_num += 1
                elif row_num + index > 14:
                    index = 0
        
        else:
            index = 0
            col_num += 1
            if col_num > 14:
                col_num = 0
                row_num += 1
                if row_num + index > 14:
                    index = 0








class miniMaxAgent():

    def __init__(self):
        self.board = [[0 for j in range(15)] for i in range(15)]
        self.maxdepth = 4

    def minimax(self, currPlayer, depth=3):
        self.maxdepth = depth
        self.bestmove = None
        score = self.minimaxHelper(currPlayer, depth, float('-inf'), float('inf'))
        row, col = self.bestmove
        return score, row, col

    def minimaxHelper(self, currPlayer, depth, alpha, beta):

        if depth <= 0:
            return eval(self.board, currPlayer) - eval(self.board, 3 - currPlayer)

        score = eval(self.board, currPlayer) - eval(self.board, 3 - currPlayer)
        moves = getMoves(self.board)
        bestmove = None

        # INSERT BLOCKING CODE/CHECK
        # THIS DOES OFFENCE 4s and 3s also!
        priority = [["xxxx", "****"], ["xxx", "***"]]
        fours = ["xxxx", "****"]
        threes = ["xxx", "***"]
        inv_BOARD = make_invert(BOARD)
        for string in priority:
            for i in range(len(string)):
                if i == ["xxxx", "****"]:
                    ind_pl = 4
                else:
                    ind_pl = 3
                if check_forward(BOARD, string[i]) != None:                               #CHECKS HORIZONTAL 4S
                    tup = check_forward(BOARD, string[i])
                    if (tup[0] -1) >= 0 and BOARD[tup[0]-1][tup[1]] == "o":          #if space before string of 4 is empty
                        self.bestmove = (tup[0] - 1, tup[1])
                    elif (tup[0] + ind_pl) <= 14 and BOARD[tup[0] + ind_pl][tup[1]] == "o":    #if space before string of 4 is full and space after string of 4s is empty
                        self.bestmove = (tup[0] + ind_pl, tup[1])
                elif check_down(inv_BOARD, string[i]) != None:                            #CHECKS VERTICAL 4S
                    tup = check_down(inv_BOARD, string[i])  
                    if (tup[0] -1) >= 0 and inv_BOARD[tup[0]-1][tup[1]] == "o":          
                        self.bestmove = (tup[0] - 1, tup[1])
                    elif (tup[0] + ind_pl) <= 14 and inv_BOARD[tup[0] + ind_pl][tup[1]] == "o":    
                        self.bestmove = (tup[0] + ind_pl, tup[1])
                elif check_diagonal(BOARD, string[i]):                                    #OH, ONLY CHECKS LEADING DIAGONLS. I CAN FLIP THE BOARD AND MAKE IT DO BOTH, BUT LET'S SEE HOW THIS GOES FIRST
                    if (tup[0] -1) >= 0 and inv_BOARD[tup[0]-1][tup[1]] == "o":         
                        self.bestmove = (tup[0] - 1, tup[1])
                    elif (tup[0] + ind_pl) <= 14 and inv_BOARD[tup[0] + ind_pl][tup[1]] == "o":    
                        self.bestmove = (tup[0] + ind_pl, tup[1])

        for score, row, col in moves:

            self.board[row][col] = currPlayer
            nextPlayer = 3 - currPlayer
            score = -self.minimaxHelper(nextPlayer, depth - 1, -beta, -alpha)
            self.board[row][col] = 0

            if score > alpha:
                alpha = score
                bestmove = (row, col)
                if alpha >= beta:
                    break

        if depth == self.maxdepth and bestmove:
            self.bestmove = bestmove

        return alpha
