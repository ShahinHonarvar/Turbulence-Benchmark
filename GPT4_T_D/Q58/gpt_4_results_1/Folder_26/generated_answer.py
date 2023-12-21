
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    width = matrix.shape[1]
    height = matrix.shape[0]

    for i in range(height):
        for j in range(width):
            for k in range(i + 1, height + 1):
                for l in range(j + 1, width + 1):
                    submatrix = matrix[i:k, j:l]
                    if np.size(submatrix) == 115:
                        count += 1
    return count
