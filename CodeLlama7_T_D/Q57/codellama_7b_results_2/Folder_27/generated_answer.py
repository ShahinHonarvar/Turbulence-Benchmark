
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize a list to store the submatrices
    submatrices = []

    # Loop over each row and column of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Calculate the sum of the elements in the submatrix
            submatrix_sum = np.sum(matrix[i:, j]) + np.sum(matrix[i, j+1:]) - matrix[i, j]
            # Check if the sum equals 77
            if submatrix_sum == 77:
                # Add the submatrix to the list of submatrices
                submatrices.append(matrix[i:, j])

    return submatrices
