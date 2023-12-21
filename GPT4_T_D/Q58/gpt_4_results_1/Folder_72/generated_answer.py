
import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, columns = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(columns):
            for x in range(i + 1, rows + 1):
                for y in range(j + 1, columns + 1):
                    submatrix = matrix[i:x, j:y]
                    if np.size(submatrix) == 16:
                        count += 1
    return count
