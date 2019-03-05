from graphics import *

def draw_sq(sX, sY, size, color, win):
    square = Rectangle(Point(sX, sY), Point(sX * 2, sY * 2))
    square.setFill(color_rgb(255,0,0))
    square.draw(win)

sqSz = 50

chWin =GraphWin("Checkers", sqSz * 10, sqSz * 10)
chWin.setCoords(0, 0, sqSz * 10, sqSz * 10)

draw_sq(sqSz, sqSz, sqSz, "red", chWin)
