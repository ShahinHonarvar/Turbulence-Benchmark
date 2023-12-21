
import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, columns = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(columns):
            for x in range(i, rows):
                for y in range(j, columns):
                    submatrix = matrix[i:x+1, j:y+1]
                    if submatrix.size == 60:
                        count += 1
    return count
