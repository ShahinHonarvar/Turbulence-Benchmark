
import numpy as np

def submatrix_with_n_numbers(matrix):
    if len(matrix.shape) != 2:
        return 0
    counter = 0
    row, col = matrix.shape
    for i in range(row):
        for j in range(col):
            for x in range(i, row):
                for y in range(j, col):
                    sub_matrix = matrix[i:x+1, j:y+1]
                    if sub_matrix.size == 130:
                        counter += 1
    return counter
