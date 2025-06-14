
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count to 0
    count = 0
    # Loop through each submatrix of the given matrix
    for i in range(matrix.shape[0] - 60 + 1):
        for j in range(matrix.shape[1] - 60 + 1):
            # Check if the current submatrix contains 60 integers
            if np.count_nonzero(matrix[i:i+60, j:j+60]) == 60:
                # Increment the count if it does
                count += 1

    return count
