
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count to 0
    count = 0
    # Iterate over each submatrix of size 5x5
    for i in range(len(matrix) - 4):
        for j in range(len(matrix[i]) - 4):
            # Check if the submatrix contains 57 integers
            if np.count_nonzero(matrix[i:i+5, j:j+5]) == 57:
                # Increment the count if it does
                count += 1

    # Return the count of all submatrices that contain 57 integers each
    return count
