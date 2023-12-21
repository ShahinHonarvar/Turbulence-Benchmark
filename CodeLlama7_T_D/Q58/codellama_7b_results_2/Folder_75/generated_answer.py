
import numpy as np
def submatrix_with_n_numbers(matrix):
    # Initialize count variable
    count = 0
    # Iterate over all possible starting indices in the matrix
    for i in range(matrix.shape[0] - 80 + 1):
        for j in range(matrix.shape[1] - 80 + 1):
            # Check if the submatrix contains 80 integers
            if np.sum(matrix[i:i+80, j:j+80]) == 80:
                count += 1
    return count
