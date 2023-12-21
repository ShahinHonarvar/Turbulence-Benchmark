
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the output list
    submatrices = []

    # Iterate over each row and column of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Get the sum of all integers in the current submatrix
            submatrix_sum = np.sum(matrix[i:,j]) + np.sum(matrix[i,j+1:])
            # If the sum is equal to -82, add the submatrix to the output list
            if submatrix_sum == -82:
                submatrices.append(matrix[i:,j])
                submatrices.append(matrix[i,j+1:])
    # Return the output list of all submatrices that have a sum equal to -82
    return submatrices
