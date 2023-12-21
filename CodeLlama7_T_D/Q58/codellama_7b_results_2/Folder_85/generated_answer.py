
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count variable
    count = 0

    # Iterate over each row of the matrix
    for i in range(matrix.shape[0] - 13 + 1):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1] - 13 + 1):
            # Check if the submatrix has 13 integers
            if sum(matrix[i:i+13, j:j+13].flatten()) == 13 * 13:
                # Increment the count variable
                count += 1

    return count
