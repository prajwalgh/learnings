import global_var
import databaseF
from collections import Counter

def create_grid_from_db()->list:
    grid=[[0 for i in range(global_var.n)] for i in range(global_var.n)]
    grid[0][1]=1
    # grid[0][2]=1
    # grid[1][2] = 1
    # grid[2][2] = 1
    # grid[5][2] = 1
    # grid[6][2] = 1
    # grid[7][2] = 1
    #
    # grid[0][3]=1
    # grid[4][1]=1
    # grid[4][1]=1
    grid[4][1]=1
    grid[5][1]=1
    grid[5][2]=1
    grid[5][3]=1
    grid[1][5]=1
    grid[2][5]=1
    grid[3][5]=1
    return grid


# databaseF.createDb()
# databaseF.store(grid)
# databaseF.retrive()
#databaseF.update("2",0)

def kill(grid,i,j):
    grid[i][j]=0

def give_life(grid,i,j):
    grid[i][j]=1

def check(grid,i, j):
    """
    Function to check surrounding cells of the current cell at position (i, j)
    and increment count based on the values of those cells.

    Parameters:
        grid (list of lists): The 2D grid representing the game board.
        i (int): The row index of the current cell.
        j (int): The column index of the current cell.

    Returns:
        count (int): The count of surrounding cells with value 1.
    """
    count = 0
    rows = len(grid)
    cols = len(grid[0])

    # Define offsets for surrounding cells
    offsets = [(-1, -1), (-1, 0), (-1, 1),
               (0, -1),           (0, 1),
               (1, -1),  (1, 0),  (1, 1)]

    # Check each surrounding cell
    for di, dj in offsets:
        ni, nj = i + di, j + dj
        # Check if the surrounding cell is within the grid boundaries
        if 0 <= ni < rows and 0 <= nj < cols:
            # Increment count if the surrounding cell has value 1
            if grid[ni][nj] == 1:
                count += 1

    return count

def traverse_grid(grid):
    print(grid ,"in traverse_grid")
    for i in range(global_var.n):
        for j in range(global_var.n):
            x=check(grid,i,j)
            print(i,j,x)
            if x>=3:
                give_life(grid,i, j)
            else:
                kill(grid,i,j)
    return grid
#
# i=3
# while i:
#     i-=1
#     # traverse_grid()
#     c=[Counter(i)for i in grid]
#     print(c)
#     print("===========================================================================================")
#     print(grid)