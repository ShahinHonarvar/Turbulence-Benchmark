
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count to 0
    count = 0
    # Loop over all possible starting indices of the submatrix
    for i in range(matrix.shape[0] - 7 + 1):
        for j in range(matrix.shape[1] - 7 + 1):
            # Check if the current submatrix contains 7 integers each
            if np.count_nonzero(matrix[i:i+7, j:j+7]) == 7 * 7:
                # Increment the count if the condition is met
                count += 1

    # Return the count of all submatrices that contain 7 integers each
    return count
