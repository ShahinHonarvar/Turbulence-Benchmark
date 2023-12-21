
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices
    submatrices = []

    # Loop over each row and column of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Find all submatrices with the desired sum
            if np.sum(matrix[i:, j]) == -15:
                submatrices.append(matrix[i:, j])

    # Return the list of submatrices
    return submatrices
