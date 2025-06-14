
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize count to 0
    count = 0
    # Loop over all possible starting positions in the matrix
    for i in range(matrix.shape[0] - 21 + 1):
        for j in range(matrix.shape[1] - 21 + 1):
            # Check if the current submatrix contains 21 integers
            if np.count_nonzero(matrix[i:i+21, j:j+21]) == 21:
                # Increment count if it does
                count += 1

    # Return count
    return count
