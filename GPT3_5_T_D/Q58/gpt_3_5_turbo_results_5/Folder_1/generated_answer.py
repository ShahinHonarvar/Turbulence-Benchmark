
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    r, c = matrix.shape
    for i in range(r):
        for j in range(c):
            if i+1 < r and j+1 < c:
                sub_matrix = matrix[i:i+2, j:j+2]
                if np.sum(sub_matrix) == 23:
                    count += 1
    return count
