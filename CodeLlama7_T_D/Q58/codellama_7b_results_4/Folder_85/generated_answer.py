
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count variable
    count = 0

    # Loop over all possible starting positions in the matrix
    for i in range(matrix.shape[0] - 13 + 1):
        for j in range(matrix.shape[1] - 13 + 1):
            # Check if the current submatrix has 13 integers each
            if np.all(matrix[i:i+13, j:j+13] == 1)):
                count += 1

    # Return the count of all submatrices that contain 13 integers each
    return count
