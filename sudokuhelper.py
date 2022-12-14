#!/bin/python3

"""Experiments in assisting a human sudoku player by simulating human logic"""

__author__ = "Adam Karl"

from termcolor import colored, cprint

def isGridValid(grid):
    """Given a sudoku grid that may or may not be complete,
    determine if the grid breaks any rules 
    (a number more than once in a row/column/cluster)
    Return True if the grid is valid, False if it breaks a rule"""
    
    # check grid dimensions
    if len(grid) != 9 or len(grid[0]) != 9:
        print(f"size: {len(grid)} x {len(grid[0])}")
        return False
    
    # check rows for duplicate values
    for r in range(9):
        found = list()
        for c in range(9):
            if grid[r][c] > 0 and grid[r][c] in found:
                return False 
            else:
                found.append(grid[r][c])
                
    # check cols for duplicate values
    for c in range(9):
        found = list()
        for r in range(9):
            if grid[r][c] > 0 and grid[r][c] in found:
                return False 
            else:
                found.append(grid[r][c])
    
    # check 3x3 clusters for duplicate values
    for i in [0,3,6]:
        for j in [0,3,6]:
            found = list()
            for r in [i,i+1,i+2]:
                for c in [j,j+1,j+2]:
                    if grid[r][c] > 0 and grid[r][c] in found:
                        return False 
                    else:
                        found.append(grid[r][c])
                        
    return True

def printChar(c, highlight=False):
    """Helper function for printGrid that prints individual cell of sudoku grid"""
    s = str(c)
    if c == 0:
        s = ' '
    
    if highlight == True:
        s = colored(s, 'yellow', attrs=['reverse', 'blink'])

    print(s, end='')
    
def printGrid(grid, x=-1, y=-1):
    """Format and print out sudoku grid
    If x and y values are given, highlight that cell"""
    # check grid dimensions
    if len(grid) != 9 or len(grid[0]) != 9:
        return
    
    for r in range (9):
        for c in range(3):
            if r==x and c==y:
                printChar(grid[r][c], True)
            else:
                printChar(grid[r][c])
                
        print('|', end='')
        
        for c in range(3,6):
            if r==x and c==y:
                printChar(grid[r][c], True)
            else:
                printChar(grid[r][c])
                
        print('|', end='')
        
        for c in range(6,9):
            if r==x and c==y:
                printChar(grid[r][c], True)
            else:
                printChar(grid[r][c])
        print()    
        
        # print horizontal lines  
        if r == 2 or r == 5:
            print("-----------")
    print()
    
def sudokuSolver(grid):
    """Given a 9x9 sudoku grid with some numbers filled, solve the puzzle and
    return the solved grid"""
    if isGridValid(grid) == False:
        print("Error: invalid grid")
        return None
    
    blankCells = list() #will contain tuples of modified cells
    
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                blankCells.append([r,c])
    
    print(f"{len(blankCells)} cells to solve")
    
    i = 0
    iterations = 0
    while i < len(blankCells):
        iterations += 1
        
        r, c = blankCells[i]
        grid[r][c] += 1
        
        if grid[r][c] == 10:
            # cycled too far, a mistake was made before this point
            grid[r][c] = 0
            i -= 1
        else:
            if isGridValid(grid) == True:
                i += 1

    print(f"solved in {iterations} iterations\n")
    return grid

def suggestNext(grid):
    """Given a sudoku puzzle, return coordinates where the human player should look to 
    make progress (if any)"""
    return 1, 2
    

def main():
    grid = [
        [0,8,0,6,4,0,0,0,7],
        [7,6,0,5,3,0,9,0,0],
        [0,0,0,0,2,7,0,0,3],
        [1,4,0,9,6,2,0,7,0],
        [2,0,0,3,7,0,0,0,1],
        [0,7,0,0,8,0,4,2,9],
        [5,1,0,0,9,6,8,0,0],
        [0,0,0,0,0,8,7,0,5],
        [0,0,0,7,0,0,0,9,6]]
    
    if isGridValid(grid) == True:
        print("Valid Grid")
    else:
        print("INVALID GRID")
        
    xHint, yHint = suggestNext(grid)
    printGrid(grid, xHint, yHint)
    
    solvedGrid = sudokuSolver(grid.copy())
    
    if isGridValid(solvedGrid) == True:
        print("Valid Grid")
    else:
        print("INVALID GRID")
    printGrid(solvedGrid)

if __name__ == "__main__":
    main()
        