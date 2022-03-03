from graphics import *
import numpy as np


def isClicked(rect, mousePos):
    p1 = rect.getP1()
    p2 = rect.getP2()
    # print(p2.x)
    if (mousePos.x > p2.x) & (mousePos.x < p1.x) & (mousePos.y > p1.y) & (mousePos.y < p2.y):
        return 1
    else:
        return 0

def main():
    win = GraphWin('ExampleWindow', 750, 750)
    rects = []
    for i in range(15):
        newRect = []
        for j in range(15):
            newSubRect = Rectangle(Point(50*(j+1), i*50), Point(j*50, 50*(i+1)))
            newSubRect.setFill('purple')
            newRect.append(newSubRect)
        rects.append(newRect)
    for rect in rects:
        for subRect in rect:
            subRect.draw(win)
    i = 1
    while True:
        mousePos = win.getMouse()
        for rect in rects:
            for subRect in rect:
                if isClicked(subRect, mousePos):
                    if i == 1:
                        subRect.setFill("black")
                        i = 2
                    else:
                        subRect.setFill("white")
                        i = 1
    win.close()

if __name__ == '__main__':
    main()
