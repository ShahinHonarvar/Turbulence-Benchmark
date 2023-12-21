
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count variable
    count = 0

    # Iterate over all possible submatrices of the given matrix
    for i in range(matrix.shape[0] - 2):
        for j in range(matrix.shape[1] - 2):
            # Check if the current submatrix contains 27 integers
            if np.count_nonzero(matrix[i:i+3, j:j+3]) == 27:
                # Increment the count variable if the condition is met
                count += 1

    # Return the count of all submatrices that contain 27 integers each
    return count
