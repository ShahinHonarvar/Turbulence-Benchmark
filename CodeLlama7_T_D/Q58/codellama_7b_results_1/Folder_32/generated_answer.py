
import numpy as np
def submatrix_with_n_numbers(matrix):
    # Initialize the count of submatrices with 103 integers each
    count = 0
    # Iterate over all possible starting positions for a submatrix
    for i in range(matrix.shape[0] - 99):
        for j in range(matrix.shape[1] - 99):
            # Check if the current submatrix contains 103 integers each
            if np.count_nonzero(matrix[i:i+100, j:j+100]) == 10000:
                count += 1
    return count
