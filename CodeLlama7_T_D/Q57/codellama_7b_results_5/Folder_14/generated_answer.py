
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []

    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):

        # Loop over each column of the matrix
        for j in range(matrix.shape[1]):

            # Find the sum of all integers in the submatrix
            sum = np.sum(matrix[i:, j]) + np.sum(matrix[i, j+1:]) - 2 * np.sum(matrix[i, j])

            # If the sum is equal to -93, add the submatrix to the list of submatrices
            if sum == -93:
                submatrices.append(matrix[i:, j] + matrix[i, j+1:])

    return submatrices
