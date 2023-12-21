
import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = np.shape(matrix)

    # finding submatrices of different sizes and checking their sum
    for submatrix_size in range(1, min(rows, cols) + 1):
        for row in range(rows - submatrix_size + 1):
            for col in range(cols - submatrix_size + 1):
                submatrix = matrix[row:row+submatrix_size, col:col+submatrix_size]

                if np.sum(submatrix) == 92:
                    result.append(submatrix)

    return result
