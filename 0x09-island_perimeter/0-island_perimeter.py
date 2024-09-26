#!/usr/bin/python3
"""A function that returns the perimeter of the island
   described in grid.
"""


def island_perimeter(grid):
    """Returns the perimeter described in grid."""
    prmt = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                if i == 0 or grid[i - 1][j] == 0:
                    prmt += 1
                if i == len(grid) - 1 or grid[i + 1][j] == 0:
                    prmt += 1
                if j == 0 or grid[i][j - 1] == 0:
                    prmt += 1
                if j == len(grid[0]) - 1 or grid[i][j + 1] == 0:
                    prmt += 1

    return prmt
