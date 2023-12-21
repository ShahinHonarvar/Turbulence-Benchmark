
import numpy as np

def submatrix_with_n_numbers(matrix, n):
    # Initialize variables for counting submatrices
    count = 0
    rows = matrix.shape[0]
    cols = matrix.shape[1]

    # Loop through each row and column of the matrix
    for i in range(rows):
        for j in range(cols):
            # Check if the current element is equal to n
            if matrix[i, j] == n:
                # Increment count by 1
                count += 1

    return count
