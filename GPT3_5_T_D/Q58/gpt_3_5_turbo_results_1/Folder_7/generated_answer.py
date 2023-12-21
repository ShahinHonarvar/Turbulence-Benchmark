
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = len(matrix), len(matrix[0])
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 121:
                for x in range(i, rows):
                    for y in range(j, cols):
                        if matrix[x][y] == 121 and (x - i + 1) * (y - j + 1) == 121:
                            count += 1
    
    return count
