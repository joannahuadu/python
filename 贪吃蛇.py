#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random
import pygame
import sys
from pygame.locals import *

Snakespeed = 8
Window_Width = 800
Window_Height = 500
Cell_Size = 20  # Width and height of the cells
# Ensuring that the cells fit perfectly in the window. eg if cell size was
# 10     and window width or windowheight were 15 only 1.5 cells would
# fit.
assert Window_Width % Cell_Size == 0, "Window width must be a multiple of cell size."
# Ensuring that only whole integer number of cells fit perfectly in the window.
assert Window_Height % Cell_Size == 0, "Window height must be a multiple of cell size."
Cell_W = int(Window_Width / Cell_Size)  # Cell Width
Cell_H = int(Window_Height / Cell_Size)  # Cellc Height

White = (255, 255, 255)
Black = (0, 0, 0)
Red = (255, 0, 0)  # Defining element colors for the program.
Green = (0, 255, 0)
DARKGreen = (0, 155, 0)
DARKGRAY = (40, 40, 40)
YELLOW = (255, 255, 0)
Red_DARK = (150, 0, 0)
BLUE = (0, 0, 255)
BLUE_DARK = (0, 0, 150)
COLOR1=(205,112,84)
COLOR2=(139,76,57)
CHOCOLATE1=(255,127,36)

BGCOLOR = COLOR1  # Background color

UP = 'up'
DOWN = 'down'  # Defining keyboard keys.
LEFT = 'left'
RIGHT = 'right'

HEAD = 0  # Syntactic sugar: index of the snake's head
globalScore=0

def main():
    global SnakespeedCLOCK, DISPLAYSURF, BASICFONT

    pygame.init()
    SnakespeedCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((Window_Width, Window_Height))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('贪吃蛇')

    startScreen()
    while True:
        runGame()
        gameoverScreen()


def runGame():
    # Set a random start point.
    startx = random.randint(5, Cell_W - 6)
    starty = random.randint(5, Cell_H - 6)
    wormCoords = [{'x': startx, 'y': starty},
                  {'x': startx - 1, 'y': starty},
                  {'x': startx - 2, 'y': starty}]
    direction = RIGHT

    # Start the apple in a random place.
    apple = getRandomLocation()

    while True:  # main game loop
        for event in pygame.event.get():  # event handling loop
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_LEFT) and direction != RIGHT:
                    direction = LEFT
                elif (event.key == pygame.K_RIGHT) and direction != LEFT:
                    direction = RIGHT
                elif (event.key == pygame.K_UP) and direction != DOWN:
                    direction = UP
                elif (event.key == pygame.K_DOWN) and direction != UP:
                    direction = DOWN
                elif event.key == pygame.K_ESCAPE:
                    terminate()

        # check if the Snake has hit itself or the edge
        if wormCoords[HEAD]['x'] == -1 or wormCoords[HEAD]['x'] == Cell_W or wormCoords[HEAD]['y'] == -1 or \
                wormCoords[HEAD]['y'] == Cell_H:
            return  # game over
        for wormBody in wormCoords[1:]:
            if wormBody['x'] == wormCoords[HEAD]['x'] and wormBody['y'] == wormCoords[HEAD]['y']:
                return  # game over

        # check if Snake has eaten an apply
        if wormCoords[HEAD]['x'] == apple['x'] and wormCoords[HEAD]['y'] == apple['y']:
            # don't remove worm's tail segment
            apple = getRandomLocation()  # set a new apple somewhere
        else:
            del wormCoords[-1]  # remove worm's tail segment

        # move the worm by adding a segment in the direction it is moving
        if direction == UP:
            newHead = {'x': wormCoords[HEAD]['x'],
                       'y': wormCoords[HEAD]['y'] - 1}
        elif direction == DOWN:
            newHead = {'x': wormCoords[HEAD]['x'],
                       'y': wormCoords[HEAD]['y'] + 1}
        elif direction == LEFT:
            newHead = {'x': wormCoords[HEAD][
                                'x'] - 1, 'y': wormCoords[HEAD]['y']}
        elif direction == RIGHT:
            newHead = {'x': wormCoords[HEAD][
                                'x'] + 1, 'y': wormCoords[HEAD]['y']}
        wormCoords.insert(0, newHead)
        DISPLAYSURF.fill(BGCOLOR)
        drawGrid()
        drawWorm(wormCoords)
        drawApple(apple)
        drawScore(len(wormCoords) - 3)

        pygame.display.update()
        SnakespeedCLOCK.tick(Snakespeed)


def drawPressKeyMsg():
    pressKeySurf1 = BASICFONT.render('Press Space to play.', True, COLOR2)
    pressKeySurf2 = BASICFONT.render('Press Esc to quit.', True, COLOR2)
    pressKeySurf3 = BASICFONT.render('Press Key Up-Down-Left-Right', True, COLOR2)
    pressKeyRect1 = pressKeySurf1.get_rect()
    pressKeyRect2 = pressKeySurf2.get_rect()
    pressKeyRect3 = pressKeySurf2.get_rect()
    pressKeyRect1.topleft = (Window_Width - 200, Window_Height - 60)
    pressKeyRect2.topleft = (Window_Width - 200, Window_Height - 30)
    pressKeyRect3.topleft = (20, Window_Height - 45)
    DISPLAYSURF.blit(pressKeySurf1, pressKeyRect1)
    DISPLAYSURF.blit(pressKeySurf2, pressKeyRect2)
    DISPLAYSURF.blit(pressKeySurf3, pressKeyRect3)


def checkForKeyPress():
    if len(pygame.event.get(pygame.QUIT)) > 0:
        terminate()
    keyUpEvents = pygame.event.get(pygame.KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == pygame.K_ESCAPE:
        terminate()
    return keyUpEvents[0].key


def startScreen():
    titleFont1 = pygame.font.SysFont('SimHei', 90)
    titleSurf1 = titleFont1.render(u"贪吃蛇", True,COLOR2)
    titleFont2 = pygame.font.Font('freesansbold.ttf', 40)
    titleSurf2 = titleFont2.render("snakes", True,COLOR2)
    degrees1 = 0
    degrees2 = 0
    while True:
        DISPLAYSURF.fill(BGCOLOR)
        rotatedSurf1 = pygame.transform.rotate(titleSurf1, degrees1)
        rotatedRect1 = rotatedSurf1.get_rect()
        rotatedRect1.center = (Window_Width / 2, Window_Height / 2-45)
        DISPLAYSURF.blit(rotatedSurf1, rotatedRect1)
        rotatedSurf2 = pygame.transform.rotate(titleSurf2, degrees2)
        rotatedRect2 = rotatedSurf2.get_rect()
        rotatedRect2.center = (Window_Width / 2, Window_Height / 2+80)
        DISPLAYSURF.blit(rotatedSurf2, rotatedRect2)
        drawPressKeyMsg()

        if checkForKeyPress():
            pygame.event.get()  # clear event queue
            return
        pygame.display.update()
        SnakespeedCLOCK.tick(Snakespeed)
        degrees1 += 3  # rotate by 3 degrees each frame
        #degrees2 += 7  # rotate by 7 degrees each frame


def terminate():
    pygame.quit()
    sys.exit()


def getRandomLocation():
    return {'x': random.randint(0, Cell_W - 1), 'y': random.randint(0, Cell_H - 1)}


def gameoverScreen():
    gameOverFont = pygame.font.Font('freesansbold.ttf', 100)
    gameSurf = gameOverFont.render('Game', True, COLOR2)
    overSurf = gameOverFont.render('Over', True,COLOR2)
    gameRect = gameSurf.get_rect()
    overRect = overSurf.get_rect()
    gameRect.midtop = (Window_Width / 2, 30)
    overRect.midtop = (Window_Width / 2, 130)

    DISPLAYSURF.blit(gameSurf, gameRect)
    DISPLAYSURF.blit(overSurf, overRect)


    drawPressKeyMsg()
    pygame.display.update()
    pygame.time.wait(500)
    checkForKeyPress()  # clear out any key presses in the event queue

    while True:
        if checkForKeyPress():
            pygame.event.get()  # clear event queue
            return


def drawScore(score):
    scoreSurf = BASICFONT.render('Score: %s' % (score), True, White)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (Window_Width - 120, 10)
    DISPLAYSURF.blit(scoreSurf, scoreRect)


def drawWorm(wormCoords):
    for coord in wormCoords:
        x = coord['x'] * Cell_Size
        y = coord['y'] * Cell_Size
        wormSegmentRect = pygame.Rect(x, y, Cell_Size, Cell_Size)
        pygame.draw.rect(DISPLAYSURF, COLOR2, wormSegmentRect)
        #wormInnerSegmentRect = pygame.Rect(
         #   x + 4, y + 4, Cell_Size - 8, Cell_Size - 8)
        #pygame.draw.rect(DISPLAYSURF, COLOR2, wormInnerSegmentRect)


def drawApple(coord):
    x = coord['x'] * Cell_Size
    y = coord['y'] * Cell_Size
    appleRect = pygame.Rect(x, y, Cell_Size, Cell_Size)
    pygame.draw.rect(DISPLAYSURF, White, appleRect)


def drawGrid():
    for x in range(0, Window_Width, Cell_Size):  # draw vertical lines
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (x, 0), (x, Window_Height))
    for y in range(0, Window_Height, Cell_Size):  # draw horizontal lines
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (0, y), (Window_Width, y))


if __name__ == '__main__':
    try:
        main()
    except SystemExit:
         pass