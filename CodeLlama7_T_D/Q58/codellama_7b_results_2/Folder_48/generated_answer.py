
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count of submatrices with 130 integers each
    count = 0

    # Loop over all possible starting positions for a submatrix
    for i in range(matrix.shape[0] - 130 + 1):
        for j in range(matrix.shape[1] - 130 + 1):
            # Check if the submatrix has 130 integers each
            if np.sum(matrix[i:i+130, j:j+130]) == 130 * 130:
                # Increment the count of submatrices with 130 integers each
                count += 1

    # Return the count of submatrices with 130 integers each
    return count
