
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count to 0
    count = 0
    # Iterate over all possible starting indices in the matrix
    for i in range(matrix.shape[0] - 6):
        for j in range(matrix.shape[1] - 6):
            # Check if the submatrix contains 7 integers each
            if np.count_nonzero(matrix[i:i+7, j:j+7]) == 49:
                count += 1

    return count
