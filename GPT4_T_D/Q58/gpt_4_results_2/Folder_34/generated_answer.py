
import numpy as np

def submatrix_with_n_numbers(int_matrix):
    count = 0
    rows, cols = int_matrix.shape
    for i in range(rows):
        for j in range(cols):
            for x in range(i, rows):
                for y in range(j, cols):
                    submatrix = int_matrix[i:x+1, j:y+1]
                    if submatrix.size == 83:
                        count += 1
    return count
