
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the output list
    submatrices = []

    # Loop over all rows and columns of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Calculate the sum of all integers in the current submatrix
            submatrix_sum = np.sum(matrix[i:, j])

            # If the sum equals 21, add the submatrix to the output list
            if submatrix_sum == 21:
                submatrices.append(matrix[i:, j])

    # Return the output list of all submatrices with a sum equal to 21
    return submatrices
