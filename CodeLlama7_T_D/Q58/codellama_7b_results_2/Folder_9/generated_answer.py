
import numpy as np

def submatrix_with_n_numbers(matrix, n):
    # Initialize the count to 0
    count = 0
    # Loop over the rows and columns of the matrix
    for i in range(matrix.shape[0] - n + 1):
        for j in range(matrix.shape[1] - n + 1):
            # Check if the submatrix has the desired number of integers
            if np.count_nonzero(matrix[i:i+n, j:j+n]) == n * n:
                count += 1
    return count
