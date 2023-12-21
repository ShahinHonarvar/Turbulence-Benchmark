
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize count variable
    count = 0

    # Iterate over rows and columns of the matrix
    for i in range(matrix.shape[0] - 90 + 1):
        for j in range(matrix.shape[1] - 90 + 1):
            # Check if submatrix contains 90 integers
            if np.sum(matrix[i:i+90, j:j+90]) == 90:
                count += 1

    return count
