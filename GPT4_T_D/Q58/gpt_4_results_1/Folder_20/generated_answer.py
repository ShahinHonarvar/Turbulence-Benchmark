
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, columns = matrix.shape
    for i in range(rows):
        for j in range(columns):
            for x in range(i+1, rows+1):
                for y in range(j+1, columns+1):
                    if np.size(matrix[i:x, j:y]) == 49:
                        count += 1
    return count
