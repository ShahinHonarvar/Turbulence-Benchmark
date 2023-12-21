
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count variable
    count = 0

    # Iterate over all possible submatrices
    for i in range(matrix.shape[0] - 1):
        for j in range(matrix.shape[1] - 1):
            # Check if the submatrix contains 1 integer
            if matrix[i][j] == 1 and matrix[i][j + 1] == 1 and matrix[i + 1][j] == 1:
                count += 1

    return count
