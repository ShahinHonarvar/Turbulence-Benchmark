
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count variable
    count = 0

    # Iterate over all possible starting positions of a submatrix
    for i in range(matrix.shape[0] - 15 + 1):
        for j in range(matrix.shape[1] - 15 + 1):
            # Check if the current submatrix contains 15 integers each
            if np.sum(matrix[i:i+15, j:j+15]) == 15 * 15:
                # Increment the count variable
                count += 1

    # Return the count of all submatrices of the given matrix that contain 15 integers each
    return count
