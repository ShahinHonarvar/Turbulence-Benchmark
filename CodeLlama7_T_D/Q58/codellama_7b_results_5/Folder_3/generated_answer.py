
import numpy as np

def submatrix_with_n_numbers(matrix, n):
    # Initialize the count to 0
    count = 0
    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # Get the current row of the matrix
        row = matrix[i]
        # Check if the current row contains n integers
        if row.size == n:
            count += 1

    return count
