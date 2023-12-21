
import numpy as np

def submatrix_with_n_numbers(matrix, n):
    # Initialize the count to 0
    count = 0
    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Get the current row as a vector
        row = matrix[i]
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Get the current column as a vector
            col = matrix[:, j]
            # Check if the submatrix has 74 integers
            if np.count_nonzero(row) == n and np.count_nonzero(col) == n:
                # Increment the count
                count += 1

    return count
