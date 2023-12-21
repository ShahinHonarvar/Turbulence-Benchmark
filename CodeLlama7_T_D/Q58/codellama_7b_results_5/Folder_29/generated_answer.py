
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count to 0
    count = 0
    # Loop over each row of the matrix
    for i in range(matrix.shape[0] - 19 + 1):
        # Loop over each column of the matrix
        for j in range(matrix.shape[1] - 19 + 1):
            # Check if the submatrix has 19 integers
            if np.count_nonzero(matrix[i:i+19, j:j+19]) == 19:
                # Increment the count by 1
                count += 1
    # Return the count of all submatrices that contain 19 integers each
    return count
