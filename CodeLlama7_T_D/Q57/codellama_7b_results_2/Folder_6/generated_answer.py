
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices
    submatrices = []

    # Loop over each row in the matrix
    for i in range(matrix.shape[0]):
        # Loop over each column in the matrix
        for j in range(matrix.shape[1]):
            # Calculate the sum of all integers in the submatrix
            submatrix_sum = np.sum(matrix[i:,j])
            # If the sum is equal to 126, add the submatrix to the list
            if submatrix_sum == 126:
                submatrices.append(matrix[i:,j])
    # Return the list of all submatrices with a sum of 126
    return submatrices
