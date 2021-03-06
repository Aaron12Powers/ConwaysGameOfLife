from pygame.locals import *
import numpy as np
from random import randint
import pygame
import module


rotateRules = False
randomize = False
blank = True

#Define Number of Columns
columns = 159
rows = 75

#Define Cell Sizes
WIDTH = 10
HEIGHT = 10
MARGIN = WIDTH // 5

#Define Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)




cells_1 = [[module.Cell for i in range(rows)] for j in range(columns)]
cells_2 = [[module.Cell for i in range(rows)] for j in range(columns)]


for row in range(0, rows):
    for column in range(0, columns):
        cells_1[column][row]  = (module.Cell(row, column))
        cells_2[column][row]  = (module.Cell(row, column))


window_height = (((HEIGHT + MARGIN) * rows) + MARGIN) 
window_width = (((WIDTH + MARGIN) * columns) + MARGIN)

screen = pygame.display.set_mode((window_width, window_height))

pygame.display.set_caption('Conways Game of Life')

if randomize:
    module.StartRandom(cells_1, rows, columns)
elif blank:
    module.StartBlank(cells_1, rows, columns)
else:
    module.StartSim(cells_1, rows, columns)

module.RunSim(cells_1, cells_2, rows, columns)

grid = []
for row in range(6):
    grid.append([])
    for column in range(8):
        grid[row].append(0)

#pygame.init()

running = True


clock = pygame.time.Clock()

tick_count = 0

interval = 0

pause = True

speed = 41

screen.fill(GREY)
for row in range(0, rows):
    for column in range(0, columns):
        if cells_1[column][row].color == 0:
            color = WHITE
        elif cells_1[column][row].color == 1:
            color = BLACK
        else:
            color = GREY
        pygame.draw.rect(screen,
            color,
            [(MARGIN + WIDTH) * cells_1[column][row].column + MARGIN,
            (MARGIN + HEIGHT) * cells_1[column][row].row + MARGIN,
            WIDTH, HEIGHT])

#Main pygame loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            running = False  # Exit loop/ close pygame when x is clicked
        key=pygame.key.get_pressed()  #checking pressed keys
        if key[pygame.K_RETURN]: 
            if randomize:
                module.StartRandom(cells_1, rows, columns)
                module.StartRandom(cells_2, rows, columns)
            else:
                module.StartSim(cells_1, rows, columns)
                module.StartSim(cells_2, rows, columns)
        if key[pygame.K_SPACE]:
            if pause:
                pause = False
            else:
                pygame.display.set_caption('Conways Game of Life - PAUSED')
                pause = True 

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            module.FlipCell(cells_1[column][row], cells_2[column][row])


    
    # First iteration
    if tick_count % 15 == 0 and pause:
        for row in range(0, rows):
            for column in range(0, columns):
                if cells_1[column][row].color == 0:
                    color = WHITE
                elif cells_1[column][row].color == 1:
                    color = BLACK
                else:
                    color = GREY
                pygame.draw.rect(screen,
                    color,
                    [(MARGIN + WIDTH) * cells_1[column][row].column + MARGIN,
                    (MARGIN + HEIGHT) * cells_1[column][row].row + MARGIN,
                    WIDTH, HEIGHT]) 


    if tick_count % 15 == 0 and not pause:
        screen.fill(GREY)
        if interval % 2 == 1:
            module.RunSim(cells_1, cells_2, rows, columns)
            for row in range(0, rows):
                for column in range(0, columns):
                    if cells_1[column][row].color == 0:
                        color = WHITE
                    elif cells_1[column][row].color == 1:
                        color = BLACK
                    else:
                        color = GREY
                    pygame.draw.rect(screen,
                        color,
                        [(MARGIN + WIDTH) * cells_1[column][row].column + MARGIN,
                        (MARGIN + HEIGHT) * cells_1[column][row].row + MARGIN,
                        WIDTH, HEIGHT]) 
            interval += 1

        else:
            module.RunSim(cells_2, cells_1, rows, columns)
            for row in range(0, rows):
                for column in range(0, columns):
                    if cells_2[column][row].color == 0:
                        color = WHITE
                    elif cells_2[column][row].color == 1:
                        color = BLACK
                    else:
                        color = GREY
                    pygame.draw.rect(screen,
                        color,
                        [(MARGIN + WIDTH) * cells_1[column][row].column + MARGIN,
                        (MARGIN + HEIGHT) * cells_1[column][row].row + MARGIN,
                        WIDTH, HEIGHT])
            interval += 1

    #restart 
    # if not pause:
    #     if module.checkCount(cells_2, rows, columns) < rows * 2 and module.checkCount(cells_1, rows, columns) < rows * 2:
    #         module.StartSim(cells_1, rows, columns)

    tick_count += 1
    clock.tick(60)
   
    pygame.display.flip()