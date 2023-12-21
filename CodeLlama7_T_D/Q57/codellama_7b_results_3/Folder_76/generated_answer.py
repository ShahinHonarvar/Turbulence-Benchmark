
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices
    submatrices = []

    # Loop over each row and column of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Find all submatrices with a sum of -255
            if np.sum(matrix[i:, j]) == -255:
                submatrices.append(matrix[i:, j])

    # Return the list of submatrices
    return submatrices
