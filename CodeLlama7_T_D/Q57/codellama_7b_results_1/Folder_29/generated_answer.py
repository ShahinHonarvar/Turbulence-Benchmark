
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices with sum equal to 84
    submatrices = []
    # Loop over each row and column of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Find the sum of all elements in the submatrix
            sum_submatrix = np.sum(matrix[i:, j]) + np.sum(matrix[i, j+1:])
            # Check if the sum is equal to 84
            if sum_submatrix == 84:
                # Append the submatrix to the list of submatrices
                submatrices.append(matrix[i:, j] + matrix[i, j+1:])
    # Return the list of submatrices with sum equal to 84
    return submatrices
