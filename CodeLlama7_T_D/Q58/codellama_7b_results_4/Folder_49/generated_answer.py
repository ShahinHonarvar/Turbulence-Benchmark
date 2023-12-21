
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize a counter for the number of submatrices with 72 integers
    count = 0

    # Loop through each row in the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column in the matrix
        for j in range(matrix.shape[1]):
            # Check if the current submatrix has 72 integers
            if np.count_nonzero(matrix[i:, j]) == 72:
                # Increment the counter by 1
                count += 1

    # Return the final value of the counter
    return count
