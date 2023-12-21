
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count of submatrices with 57 integers each
    count = 0

    # Iterate over all possible starting positions for a submatrix
    for i in range(matrix.shape[0] - 4 + 1):
        for j in range(matrix.shape[1] - 4 + 1):
            # Check if the submatrix contains 57 integers each
            if np.sum(matrix[i:i+5, j:j+5]) == 57:
                count += 1

    return count
