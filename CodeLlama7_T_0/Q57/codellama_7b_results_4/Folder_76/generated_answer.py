
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices
    submatrices = []

    # Loop over each row and column of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Calculate the sum of all integers in the submatrix
            submatrix_sum = np.sum(matrix[i:, j]) + np.sum(matrix[i, j+1:])

            # If the sum is equal to -255, add the submatrix to the list
            if submatrix_sum == -255:
                submatrices.append(matrix[i:, j] + matrix[i, j+1:])

    # Return the list of all submatrices that have a sum equal to -255
    return submatrices
