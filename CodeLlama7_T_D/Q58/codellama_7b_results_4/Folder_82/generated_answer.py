
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count of submatrices with 99 integers each
    count = 0

    for i in range(matrix.shape[0] - 1):
        for j in range(matrix.shape[1] - 1):
            # Check if the current submatrix contains 99 integers
            if (matrix[i:i+2, j:j+2] == 99).all():
                count += 1

    return count
