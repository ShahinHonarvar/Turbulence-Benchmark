
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count of submatrices with 95 integers each
    count = 0

    # Loop over all rows and columns in the matrix
    for i in range(matrix.shape[0] - 1):
        for j in range(matrix.shape[1] - 1):
            # Check if the current submatrix has 95 integers each
            if np.count_nonzero(matrix[i:i+2, j:j+2]) == 95:
                # Increment the count of submatrices with 95 integers each
                count += 1

    # Return the count of submatrices with 95 integers each
    return count
