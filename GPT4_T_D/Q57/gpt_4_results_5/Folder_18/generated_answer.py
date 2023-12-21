
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for size in range(1, min(rows, cols) + 1):  # size of submatrix
        for i in range(0, rows - size + 1):  # row index
            for j in range(0, cols - size + 1):  # col index
                submatrix = matrix[i:i+size, j:j+size]
                if np.sum(submatrix) == 616:
                    result.append(submatrix)
    return result
