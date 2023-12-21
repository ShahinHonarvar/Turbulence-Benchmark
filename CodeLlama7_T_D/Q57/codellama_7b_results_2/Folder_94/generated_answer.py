
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices
    submatrices = []

    # Loop over all possible starting rows and columns
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Find the sum of all integers in the submatrix
            submatrix_sum = np.sum(matrix[i:, j]) + np.sum(matrix[i, j+1:])
            if submatrix_sum == 92:
                # If the sum is equal to 92, add the submatrix to the list of submatrices
                submatrices.append(matrix[i:, j])
                submatrices.append(matrix[i, j+1:])
    return submatrices
