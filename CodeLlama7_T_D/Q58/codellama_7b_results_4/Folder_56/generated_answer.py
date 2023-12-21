
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count of submatrices with 68 integers each to 0
    count = 0
    # Loop over all possible starting positions for a submatrix
    for i in range(matrix.shape[0] - 5):
        for j in range(matrix.shape[1] - 5):
            # Check if the current submatrix has 68 integers each
            if np.count_nonzero(matrix[i:i+6, j:j+6]) == 68:
                # Increment the count of submatrices with 68 integers each
                count += 1

    return count
