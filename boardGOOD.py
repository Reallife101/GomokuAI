from graphics import *
import numpy as np
from myAI2 import *
import time

def isClicked(rect, mousePos):
    p1 = rect.getP1()
    p2 = rect.getP2()
    # print(p2.x)
    if (mousePos.x > p2.x) & (mousePos.x < p1.x) & (mousePos.y > p1.y) & (mousePos.y < p2.y):
        return 1
    else:
        return 0


def main():
    turn = 0

    win0 = GraphWin('ExampleWindow0', 750, 750)
    second = Rectangle(Point(350, 300), Point(20, 400))
    second.setFill('white')
    first = Rectangle(Point(730, 300), Point(360, 400))
    first.setFill('black')

    first.draw(win0)
    second.draw(win0)

    while turn == 0:
        selects = win0.getMouse()
        if isClicked(first, selects):
            turn = 1
        elif isClicked(second, selects):
            turn = 2

    win0.close()
    print(turn)



    # hidden_board = [[0 for j in range(15)] for i in range(15)]


    win = GraphWin('ExampleWindow', 750, 750)
    rects = []
    for i in range(15):
        newRect = []
        for j in range(15):
            newSubRect = Rectangle(Point(50 * (j + 1), i * 50), Point(j * 50, 50 * (i + 1)))
            newSubRect.setFill('purple')
            newRect.append(newSubRect)
        rects.append(newRect)
    for rect in rects:
        for subRect in rect:
            subRect.draw(win)
    i = 1
    aiAgent = miniMaxAgent()
    # aiAgent.board = hidden_board
    mousepos = None
    while not checkWinner(aiAgent.board, i):
        print(i)
        score, row, col = None, -1, -1
        if i != turn:
            print('turn')
            score, row, col = aiAgent.minimax(turn, depth=2)
            print('update board')
            aiAgent.board[row][col] = (1 if turn != 1 else 2)
        else:
            mousepos = win.getMouse()

        turn_played = False
        for a, rect in enumerate(rects):
            for b, subRect in enumerate(rect):
                if i == turn: # it is the human's turn
                    if isClicked(subRect, mousepos):
                        print('update board 2')
                        if aiAgent.board[a][b] == 0:
                            aiAgent.board[a][b] = turn
                        if i == 1:
                            subRect.setFill("black")
                            i = 2
                            turn_played = True
                        else:
                            subRect.setFill("white")
                            i = 1
                            turn_played = True
                else: # agent turn
                    if row == a and col == b:
                        if i == 1:
                            subRect.setFill("black")
                            i = 2
                            turn_played = True
                        else:
                            subRect.setFill("white")
                            i = 1
                            turn_played = True
                if turn_played:
                    break
            if turn_played:
                break
                # if i == 1:
                #     subRect.setFill("black")
                #     i = 2
                # else:
                #     subRect.setFill("white")
                #     i = 1
    print("win win")
    time.sleep(2)
    win.close()


if __name__ == '__main__':
    main()

# chessboard = [[0 for j in range(board_size)] for i in range(board_size)]
# agent1 = myAI2.miniMaxAgent()
# agent1.board = chessboard
# agent2 = myAI2.miniMaxAgent()
# agent2.board = chessboard
#
# while True:
#     while not winner:
#         start_time = pygame.time.get_ticks()  # start turn timer
#
#         if currPlayer == player1 and p1_controls == 'human':
#             row, col = clickToPos()
#             while not validatePos((row, col), chessboard):
#                 row, col = clickToPos()
#
#         elif currPlayer == player1 and p1_controls == 'computer':
#             score, row, col = agent1.minimax(1, 2)
#
#         elif currPlayer == player2 and p2_controls == 'human':
#             row, col = clickToPos()
#             while not validatePos((row, col), chessboard):
#                 row, col = clickToPos()
#
#         elif currPlayer == player2 and p2_controls == 'computer':
#             score, row, col = agent2.minimax(2, 2)
#
#         chessboard[row][col] = currPlayer
#         winner = checkWinner(chessboard, currPlayer)
#         posToPiece((row, col), currPlayer)
