
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices
    submatrices = []

    # Loop over each row and column of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Calculate the sum of all elements in the submatrix
            submatrix_sum = np.sum(matrix[i:, j:])

            # Check if the sum is equal to 398
            if submatrix_sum == 398:
                # Add the submatrix to the list of submatrices
                submatrices.append(matrix[i:, j:])

    # Return the list of submatrices
    return submatrices
