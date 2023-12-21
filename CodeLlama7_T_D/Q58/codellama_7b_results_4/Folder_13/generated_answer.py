
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count of submatrices with 175 integers each
    count = 0
    # Iterate over all possible starting positions of a submatrix
    for i in range(len(matrix) - 1):
        for j in range(i + 1, len(matrix)):
            # Check if the current submatrix has 175 integers each
            if np.count_nonzero(matrix[i:j]) == 175:
                count += 1
    return count
