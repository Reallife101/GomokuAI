'''
def checkInARow(arr: [str], color, num):
    cont = 0
    for i in arr:
        if i == ('B' if color == 0 else 'W'):
            cont += 1
            if cont >= num:
                return (i, arr, color) #first last space in a series of num in the array
        else:
            cont = 0
    return -1


def checkInARowBoard(board, color, num):        #check for rows in board
    cont = 0
    for j in board:
        for i in j:
            if i == ('B' if color == 0 else 'W'):
                cont += 1
                if cont >= num:
                    return (i, j, color) #first last space in a series of num in the array
            else:
                cont = 0
    return -1
'''
#def tileLocation(board, array, i):
    #if    #only checks for a list of 5 if s




'''
def checkFour(color: int, row: int, col: int, num: int):    #returns True if need to block
    update = 1
    vert = checkInARow(getVertRow(row, col), color, num)
    horz = checkInARow(getHorRow (row, col), color, num)
    dia1 = checkInARow(getDia1Row(row, col), color, num)
    dia2 = checkInARow(getDia2Row(row, col), color, num)
    if vert[0] >-1:
        getHorizontals()
        #tileLocation


        return update
    elif horz[0] > -1:
        placePiece(horz[1], horz[0], horz[2], num)
        return update
    elif dia1[0] > -1:
        placePiece(dia1[1], dia1[0], dia1[2], num)
        return update
    elif dia2[0] > -1:
        placePiece(dia2[1], dia2[0], dia2[2], num)
        return update
    else:   #check for 2 intercepting 3s #check for 3s
        return update - 1


def CheckBad(color: int, row: int, col: int, num: int):
    checkFour(color, row, col, 4)      #which color, row, col
    #check intercepting 3s
    checkFour(color, row, col, 3)
'''
