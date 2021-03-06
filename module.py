import random

class Cell(object):
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.color = 2
        self.neighbors = 0

#setup first cell of simulation
def StartSim(cells, rows, columns):
    for row in range(0, rows):
        for column in range(0, columns):
            if cells[column][row].column != (columns // 2):
                cells[column][row].color = 0
            elif cells[column][row].row != 0:
                cells[column][row].color = 1    
            else:
                cells[column][row].color = 1


def StartRandom(cells, rows, columns):
    for row in range(0, rows):
        for column in range(0, columns):
            randomRoll = random.randint(0,100)
            if randomRoll % 5 == 0:
                cells[column][row].color = 1
            else:
                cells[column][row].color = 0

def StartBlank(cells, rows, columns):
    for row in range(0, rows):
        for column in range(0, columns):
            cells[column][row].color = 0


def RunSim(oldCells, newCells, rows, columns):
    for row in range(0, rows):
        for column in range(0, columns):
            getNeighbors(oldCells, row, column)
            if isUnderpop(oldCells[column][row].neighbors):
                newCells[column][row].color = 0
            elif isOverpop(oldCells[column][row].neighbors):
                newCells[column][row].color = 0
            elif birth(oldCells[column][row].neighbors):
                newCells[column][row].color = 1
            else:
                newCells[column][row].color = oldCells[column][row].color

def getNeighbors(oldCells, row, column):
    oldCells[column][row].neighbors = 0
    try:
        if oldCells[column-1][row-1].color == 1:
            oldCells[column][row].neighbors += 1
        if oldCells[column][row-1].color == 1:
            oldCells[column][row].neighbors += 1

        if oldCells[column+1][row-1].color == 1:
            oldCells[column][row].neighbors += 1

        if oldCells[column-1][row].color == 1:
            oldCells[column][row].neighbors += 1

        if oldCells[column+1][row].color == 1:
            oldCells[column][row].neighbors += 1

        if oldCells[column-1][row+1].color == 1:
            oldCells[column][row].neighbors += 1

        if oldCells[column][row+1].color == 1:
            oldCells[column][row].neighbors += 1

        if oldCells[column+1][row+1].color == 1:
            oldCells[column][row].neighbors += 1
    except:
        oldCells[column][row].neighbors = 0


def isUnderpop(neighbors):
    if neighbors < 2:
        return True
    else:
        return False

def isOverpop(neighbors):
    if neighbors > 3:
        return True
    else:
        return False

def birth(neighbors):
    if neighbors == 3:
        return True
    else:
        return False

def checkCount(cells, rows, columns):
    count = 0
    for row in range(0, rows):
        for column in range(0, columns):
            if cells[column][row].color == 1:
                count += 1
    print(count)
    return count

def FlipCell(cell_1, cell_2):
    if cell_1.color == 0 and cell_2.color == 0:
        cell_1.color = 1
        cell_2.color = 1
    elif cell_1.color == 0 and cell_2.color == 1:
        cell_1.color = 1
        cell_2.color = 0
    elif cell_1.color == 1 and cell_2.color == 0:
        cell_1.color = 0
        cell_2.color = 1
    elif cell_1.color == 1 and cell_2.color == 1:
        cell_1.color = 0
        cell_2.color = 0