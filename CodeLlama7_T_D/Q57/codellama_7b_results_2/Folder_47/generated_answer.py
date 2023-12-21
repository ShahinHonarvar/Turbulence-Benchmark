
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []

    # Iterate over each row and column of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Find all submatrices with a sum equal to 27
            if np.sum(matrix[i:, j]) == 27 or np.sum(matrix[i, j:]) == 27:
                # Add the submatrix to the list of submatrices
                submatrices.append(matrix[i:, j])
                submatrices.append(matrix[i, j:])

    return submatrices
