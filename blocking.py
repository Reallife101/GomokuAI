# Put your functions in here.
# Feel free to run your design past me before beginning to implement.
#list1 = ['EOARBRNIAB', 'ZEBRAEBRBH', 'ARRACCOONR', 'AACBRRCHEC', 'CNABOZOBKA', 'BONIRBBNCA', 'EERTCBRAIA', 'ABCERICRHR', 'BOIORORCCO', 'BOAAKRKEAR']


'''
legit_puzzle = ["WAQHGTTWEE",
                "CBMIVQQELS",
                "APXWKWIIIL",
                "LDELFXPIPV",
                "PONDTMVAMN",
                "OEDSOYQGOB",
                "LGQCKGMMCT",
                "YCSLOACUZM",
                "XVDMGSXCYZ",
                "UUIUNIXFNU"]
'''

def make_legit_puzzle(puzzle):
    legit_puzzle = []
    start = 0
    end = 10
    while end <= 100:
        row = puzzle[start: end]
        start += 10
        end +=10
        legit_puzzle.append(row)
    return legit_puzzle

def make_reverse_puzzle(legit_puzzle):
    rev_puzzle = []
    for row in legit_puzzle:
        rev = []
        for i in range(len(row)-1, -1, -1):
            rev.append(row[i])
        rev_str = "".join(rev)
        rev_puzzle.append(rev_str)
    return rev_puzzle

def make_column_row(legit_puzzle, j):
    column = []
    for row in legit_puzzle:
        column.append(row[j])
    string_column = ''.join(column)
    return string_column


def make_invert(legit_puzzle):
   invert = []
   for j in range(0,10):
      column = make_column_row(legit_puzzle, j)
      invert.append(column)
   return invert
def make_reverse_invert(invert):
    rev_invert = []
    for row in invert:
        rev = []
        for i in range(len(row)-1, -1, -1):
            rev.append(row[i])
        rev_str = "".join(rev)
        rev_invert.append(rev_str)
    return rev_invert
#invert = make_invert(legit_puzzle)
#print(make_reverse_invert(invert))


'''
def reverse_word(word):
   rev = []
   for i in range(len(word)-1, -1, -1): 
      rev.append(word[i])
   return ''.join(rev)
'''
#####################
def check_forward(legit_puzzle, word):
    row_num = 0
    while row_num <= 9:
        if legit_puzzle[row_num].find(word) != -1:
            col_num = legit_puzzle[row_num].find(word)
            return (row_num, col_num)
        row_num += 1
    #else:
        #pass
#####################
def check_backward(rev_puzzle, word): 
    row_num = 0
    while row_num <= 9:
        if rev_puzzle[row_num].find(word) != -1:
            col_num = 9 - rev_puzzle[row_num].find(word)
            #return word + ": (BACKWARD) row: " + str(row_num) + " column: " + str(column)
            return (row_num, col_num)
        row_num += 1
    #else:
        #pass

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

def check_up(rev_invert, word):
    col_num = 0
    while col_num <= 9:
        if rev_invert[col_num].find(word) != -1:
            row_num = 9 - rev_invert[col_num].find(word)
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
            elif col_num >= 9: #this is just to catch row_num and col_num, nothing to do with indicies
                col_num = 0
                row_num += 1
                if row_num + index > 9:
                    index = 0
                    col_num += 1
            elif row_num + index > 9:
                index = 0 #check to make sure the index resets to 0
                col_num += 1
                if col_num > 9:
                    col_num = 0
                    row_num += 1
            elif col_num + index > 9:
                index = 0 #check to make sure the index resets to 0
                col_num += 1
                if col_num > 9:
                    col_num = 0
                    row_num += 1
                elif row_num + index > 9:
                    index = 0
        
        else:
            index = 0
            col_num += 1
            if col_num > 9:
                col_num = 0
                row_num += 1
                if row_num + index > 9:
                    index = 0

