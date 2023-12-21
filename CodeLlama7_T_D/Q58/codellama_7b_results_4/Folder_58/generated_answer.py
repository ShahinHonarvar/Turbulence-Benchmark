
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count of submatrices with 185 integers each
    count = 0
    # Iterate over all possible starting positions of a submatrix
    for i in range(matrix.shape[0] - 184):
        for j in range(matrix.shape[1] - 184):
            # Check if the current submatrix contains 185 integers each
            if all(all(matrix[k, l] == 185) for k in range(i, i + 185)) for l in range(j, j + 185)):
                count += 1
    return count
