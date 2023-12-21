
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices
    submatrices = []

    # Loop over each row and column of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Get the sum of all integers in the submatrix
            submatrix_sum = matrix[i:i+1, j:j+1].sum()
            # If the sum is equal to -10, add the submatrix to the list
            if submatrix_sum == -10:
                submatrices.append(matrix[i:i+1, j:j+1])
    # Return the list of all submatrices that have a sum of -10
    return submatrices
