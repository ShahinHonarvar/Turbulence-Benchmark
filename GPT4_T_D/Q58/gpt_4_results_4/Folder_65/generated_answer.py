
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for x in range(rows):
        for y in range(cols):
            for i in range(x+1, rows+1):
                for j in range(y+1, cols+1):
                    submat = matrix[x:i, y:j]
                    if submat.size == 35:
                        count += 1
    return count
