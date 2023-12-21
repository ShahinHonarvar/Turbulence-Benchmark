
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize a list to store the submatrices
    submatrices = []

    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop over each column of the matrix
        for j in range(matrix.shape[1]):
            # Calculate the sum of all elements in the submatrix
            submatrix_sum = np.sum(matrix[i:,j]) + np.sum(matrix[i,j+1:])

            # If the sum is equal to 77, add the submatrix to the list
            if submatrix_sum == 77:
                submatrices.append(matrix[i:,j] + matrix[i,j+1:])

    # Return the list of all submatrices that satisfy the condition
    return submatrices
