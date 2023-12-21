
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count of submatrices with 9 integers each
    count = 0

    for i in range(matrix.shape[0] - 8):
        for j in range(matrix.shape[1] - 8):
            # Check if the current submatrix has 9 integers each
            if np.all(matrix[i:i + 9, j:j + 9] == 1):
                count += 1

    return count
