
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices
    submatrices = []

    # Loop over each row and column of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Find the sum of all integers in the submatrix
            sum_submatrix = np.sum(matrix[i:, j]) + np.sum(matrix[i, j+1:]) - matrix[i, j]
            if sum_submatrix == 382:
                # Add the submatrix to the list of submatrices
                submatrices.append(matrix[i:, j])

    return submatrices
