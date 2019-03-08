from graphics import *

def draw_sq(sX, sY, size, color, win):
    square = Rectangle(Point(sX, sY), Point(sX * 2, sY * 2))
    square.setFill(color_rgb(255,0,0))
    square.draw(win)

sqSz = 50

chWin =GraphWin("Checkers", sqSz * 10, sqSz * 10)
chWin.setCoords(0, 0, sqSz * 10, sqSz * 10)

for i in range(8):
    square = Rectangle(Point(sqSz(i * 1, sqSz(i * 1)), Point(i * 2, sqSz*2))
    square.setFill(color_rgb(240,0,0))
    square.draw(chWin)

draw_sq(sqSz, sqSz, sqSz, "red", chWin)
