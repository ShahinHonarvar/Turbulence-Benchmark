
import numpy as np

def submatrix_with_particular_sum(matrix):
    possible_submatrices = []
    nrows, ncols = matrix.shape
    original_matrix = matrix.copy()

    for size in range(1, min(nrows, ncols) + 1):
        for row in range(0, nrows - size + 1):
            for col in range(0, ncols - size + 1):
                submatrix = original_matrix[row:row+size, col:col+size]
                if np.sum(submatrix) == 64:
                    possible_submatrices.append(submatrix)
    
    return possible_submatrices
