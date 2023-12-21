
import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    Returns the count of all submatrices of the given matrix that contain 96 integers each.
    If no such submatrix is found, returns 0.
    """
    n = 96
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            if np.sum(matrix[i:i+n, j:j+n]) == n**2:
                count += 1
    return count
