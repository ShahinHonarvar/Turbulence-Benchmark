
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices
    submatrices = []

    # Loop through each row and column of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Get the sum of all integers in the current submatrix
            submatrix_sum = np.sum(matrix[i:, j]) + np.sum(matrix[i, j+1:])
            # If the sum equals 1, add the submatrix to the list
            if submatrix_sum == 1:
                submatrices.append(matrix[i:, j] + matrix[i, j+1:])
    return submatrices
