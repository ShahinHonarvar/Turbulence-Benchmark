
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for x in range(i+1, rows+1):
                for y in range(j+1, cols+1):
                    submatrix = matrix[i:x, j:y]
                    if submatrix.size == 69:
                        count += 1
    return count
