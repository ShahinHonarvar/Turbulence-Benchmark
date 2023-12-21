
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count variable
    count = 0

    # Iterate over all possible submatrices of the given matrix
    for i in range(matrix.shape[0] - 74 + 1):
        for j in range(matrix.shape[1] - 74 + 1):
            # Check if the current submatrix contains 74 integers each
            if np.sum(matrix[i:i+74, j:j+74]) == 74 * 100:
                # Increment the count variable
                count += 1

    # Return the final count value
    return count
