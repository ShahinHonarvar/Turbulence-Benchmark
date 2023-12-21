
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the output list
    submatrices = []

    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop over each column of the matrix
        for j in range(matrix.shape[1]):
            # Find the sum of all integers in the submatrix
            submatrix_sum = np.sum(matrix[i:,j]) + np.sum(matrix[i,j+1:])

            # Check if the submatrix sum is equal to -863
            if submatrix_sum == -863:
                # If it is, add the submatrix to the output list
                submatrices.append(matrix[i:,j][:,np.newaxis] + matrix[i,j+1:][np.newaxis,:]))

    # Return the output list of submatrices
    return submatrices
