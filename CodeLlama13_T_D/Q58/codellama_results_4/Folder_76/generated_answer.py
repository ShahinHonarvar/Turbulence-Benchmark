
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize a counter for the number of submatrices found
    count = 0

    # Loop through each row and column in the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Find all submatrices with 159 integers starting from the current position (i, j)
            submatrices = np.lib.stride_tricks.sliding_window_view(matrix[i:, j:], (159, 159))

            # Count the number of submatrices found with 159 integers each
            count += len(submatrices)

    return count
