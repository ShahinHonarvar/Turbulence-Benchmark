
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []

    # Loop over each row and column of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Find the sum of all integers in the submatrix starting at (i, j)
            submatrix_sum = np.sum(matrix[i:, j:])

            # If the sum is equal to -185, add the submatrix to the list of submatrices
            if submatrix_sum == -185:
                submatrices.append(matrix[i:, j:])

    # Return the list of submatrices that satisfy the condition
    return submatrices
