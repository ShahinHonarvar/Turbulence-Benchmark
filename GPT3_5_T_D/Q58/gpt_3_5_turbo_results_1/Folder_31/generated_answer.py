
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    size = matrix.shape
    for i in range(size[0]):
        for j in range(size[1]):
            if i + 2 < size[0] and j + 2 < size[1]:
                submatrix = matrix[i:i+3, j:j+3].flatten()
                if len(np.unique(submatrix)) == 45:
                    count += 1
    return count
