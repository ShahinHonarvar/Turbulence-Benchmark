
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count to 0
    count = 0

    # Iterate over all possible starting positions of a submatrix
    for i in range(matrix.shape[0] - 26):
        for j in range(matrix.shape[1] - 26):
            # Check if the current submatrix contains 27 integers each
            if np.all(matrix[i:i+26, j:j+26] == 27)):
                # Increment the count if a matching submatrix is found
                count += 1

    # Return the count of all submatrices of the given matrix that contain 27 integers each
    return count
