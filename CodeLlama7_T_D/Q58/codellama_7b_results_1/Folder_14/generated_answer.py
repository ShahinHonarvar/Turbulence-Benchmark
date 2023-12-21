
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize count variable
    count = 0

    # Iterate over all possible starting positions of a submatrix
    for i in range(matrix.shape[0] - 84 + 1):
        for j in range(matrix.shape[1] - 84 + 1):
            # Check if the submatrix contains 84 integers
            if np.count_nonzero(matrix[i:i+84, j:j+84]) == 84:
                # Increment count variable
                count += 1

    # Return count variable
    return count
