from tetris import Tetris
import pygame as pg
from time import sleep

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    K_a,
    K_d,
    QUIT,
    MOUSEBUTTONDOWN,
    
)


pg.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
font = pg.font.Font('freesansbold.ttf', 16)

clock = pg.time.Clock()

t = Tetris(start_level=0)

running = True

BLOCKSIZE = 30


def drawGame(tetris_tuple):
    grid = tetris_tuple[0]
    for y in range(len(grid)):
        for x in range(len(grid[y])):

            if grid[y][x]:
                square = pg.Rect((x+1)*BLOCKSIZE, (y+1) *
                                 BLOCKSIZE, BLOCKSIZE, BLOCKSIZE)
                pg.draw.rect(screen, (255, 255, 255), square)
    showNext(tetris_tuple[1])
    showStats(tetris_tuple[2], tetris_tuple[3], tetris_tuple[4])
    pg.display.update()

def showStats(cleared_rows, level, points):
    points = points
    lines = cleared_rows
    level = level
    levelText = font.render(f"Level: {level}", True, (255,255,255))
    linesText = font.render(f"Lines: {lines} ", True, (255,255,255))
    scoreText = font.render(f"Score: {points}", True, (255,255,255))
    levelTextRect = levelText.get_rect()
    linesTextRect = linesText.get_rect()
    scoreTextRect = scoreText.get_rect()
    levelTextRect.center = (200, 720)
    linesTextRect.center = (200, 740)
    scoreTextRect.center = (200, 760)
    screen.blit(levelText, levelTextRect)
    screen.blit(linesText, linesTextRect)
    screen.blit(scoreText, scoreTextRect)


def showNext(next_piece):
    for y in range(len(next_piece)):
        for x in range(len(next_piece[y])):
            if next_piece[y][x]:
                sq = pg.Rect((x+12)*BLOCKSIZE, (y+1) *
                                 BLOCKSIZE, BLOCKSIZE, BLOCKSIZE)
                pg.draw.rect(screen, (255, 255, 255), sq)



running = True
while running:
    action = [0, 0, 0]
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_a:
                action[1] = -1
            if event.key == K_d:
                action[1] = 1
            if event.key == K_LEFT:
                action[0] = -1
            if event.key == K_RIGHT:
                action[0] = 1
            if event.key == K_DOWN:
                action[2] = 1
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 4:
                action[0] = -1
            elif event.button == 5:
                action[0] = 1
            elif event.button == 1:
                action[1] = -1
            elif event.button == 3:
                action[1] = 1
            elif event.button == 2:
                action[2] = 1


    game_state = t.gameloop(action=action)
    running = game_state[5]

    screen.fill((0, 0, 0))
    drawGame(game_state)
    clock.tick(60)
