
import numpy as np

def submatrix_with_n_numbers(matrix, n):
    # Initialize a counter for the number of submatrices found
    count = 0

    # Iterate over the rows and columns of the matrix
    for i in range(matrix.shape[0] - n + 1):
        for j in range(matrix.shape[1] - n + 1):
            # Check if the submatrix has n integers
            if np.count_nonzero(matrix[i:i+n, j:j+n]) == n:
                # Increment the counter if a submatrix with n integers is found
                count += 1

    # Return the number of submatrices found
    return count
