
import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray):
        return 0
    count = 0
    r, c = matrix.shape
    for i in range(r):
        for j in range(c):
            for x in range(i+1, r+1):
                for y in range(j+1, c+1):
                    submatrix = matrix[i:x, j:y]
                    if submatrix.size == 173:
                        count += 1
    return count
