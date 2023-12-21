
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape

    # Iterate through all possible submatrix sizes
    for submatrix_size in range(1, min(rows, cols) + 1):
        # Iterate through all possible submatrix positions
        for row in range(rows - submatrix_size + 1):
            for col in range(cols - submatrix_size + 1):
                submatrix = matrix[row:row+submatrix_size, col:col+submatrix_size]
                if np.sum(submatrix) == 862:
                    submatrices.append(submatrix)

    return submatrices
