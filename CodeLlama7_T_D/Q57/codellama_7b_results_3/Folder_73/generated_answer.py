
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices
    submatrices = []
    # Loop over each row and column of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Find the sum of all integers in the current submatrix
            sum = np.sum(matrix[i:, j]) + np.sum(matrix[i, j+1:]) - matrix[i, j]
            # If the sum is equal to 93, add the submatrix to the list
            if sum == 93:
                submatrices.append(matrix[i:, j] + matrix[i, j+1:])
    return submatrices
