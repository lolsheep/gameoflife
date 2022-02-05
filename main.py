import pygame as pg 
import sys
from random import randrange

clock = pg.time.Clock()
pg.init()
size = (1200,720)
screen = pg.display.set_mode(size)


grid = []
space_x = 0
space_y = 0

background = pg.Surface((1280,720))
background.fill((20,0,20))



for i in range(72):
    grid.append([])
    for j in range(120):
        grid[i].append(pg.Rect((space_x, space_y),(10, 10)))
        space_x += 11
    space_y += 11
    space_x = 0


matrix = [[0 for i in range(120)] for i in range(72)]
def ran_color():

    r = randrange(0,255)
    g = randrange(0,255)
    b = randrange(0,255)

    return (r,g,b)
def live(m):

    new = [[0 for i in range(120)] for i in range(72)]

    for i in range(len(m)-1):
        for j in range(len(m[i])-1):
            live = 0
            if m[i][j-1] == 1:
                live += 1
            if m[i][j+1] == 1:
                live += 1
            if m[i-1][j] == 1:
                live += 1
            if m[i-1][j+1] == 1:
                live += 1
            if m[i-1][j-1] == 1:
                live += 1

            if m[i+1][j] == 1:
                live += 1
            if m[i+1][j-1] == 1:
                live += 1
            if m[i+1][j+1] == 1:
                live += 1
 
            if m[i][j] == 1:
                if live < 2:
                    new[i][j] = 0
                elif live == 2 or live == 3:
                    new[i][j] = 1
                elif live > 3:
                    new[i][j] = 0

            else:

                if live == 3:
                    new[i][j] = 1

    return new

def render():
    c = ran_color()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                pg.draw.rect(screen, c, grid[i][j])
            else:
                pg.draw.rect(screen,(255,255,255), grid[i][j])
def done():

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                return False
    return True

go = False

while 1:

    for e in pg.event.get():

        if e.type == pg.QUIT:
            sys.exit()
        if pg.mouse.get_pressed()[0]:
            pos = pg.mouse.get_pos()
            for i in grid:
                for j in i:
                    if j.collidepoint(pos):
                        if matrix[grid.index(i)][i.index(j)] == 0:
                            go = False
                            matrix[grid.index(i)][i.index(j)] = 1
                            render()

        if e.type == pg.KEYDOWN:
            if e.key == pg.K_SPACE:
                go = True if not go == True else False
            if e.key == pg.K_x:
                matrix = [[0 for i in range(400)] for i in range(400)]
                go = False
    

    screen.fill(0)
    render()
    if go or done():
        render()
        matrix = live(matrix)

    pg.display.flip()

    clock.tick(30)