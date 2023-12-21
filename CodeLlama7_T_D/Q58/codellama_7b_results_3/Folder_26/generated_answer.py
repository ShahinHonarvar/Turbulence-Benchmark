
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count variable
    count = 0

    # Loop over all possible submatrices of the given matrix
    for i in range(matrix.shape[0] - 1):
        for j in range(matrix.shape[1] - 1):
            # Check if the current submatrix contains 115 integers each
            if np.count_nonzero(matrix[i:i+2, j:j+2]) == 115:
                # Increment the count variable if a submatrix is found that contains 115 integers each
                count += 1

    # Return the final count value
    return count
