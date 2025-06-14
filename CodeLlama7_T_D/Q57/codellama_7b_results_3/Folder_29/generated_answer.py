
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []

    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop over each column of the matrix
        for j in range(matrix.shape[1]):
            # Calculate the sum of all integers in the submatrix
            submatrix_sum = np.sum(matrix[i:, j])

            # Check if the sum is equal to 84
            if submatrix_sum == 84:
                # If so, append the submatrix to the list of submatrices
                submatrices.append(matrix[i:, j])

    # Return the list of submatrices that have a sum of all integers equal to 84
    return submatrices
