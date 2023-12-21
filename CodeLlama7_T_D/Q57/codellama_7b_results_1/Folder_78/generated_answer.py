
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize a list to store the submatrices
    submatrices = []

    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Calculate the sum of all integers in the submatrix
            submatrix_sum = np.sum(matrix[i:, j])

            # Check if the sum is equal to 17
            if submatrix_sum == 17:
                # If the sum is equal to 17, add the submatrix to the list of submatrices
                submatrices.append(matrix[i:, j])

    # Return the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals 17. If no such submatrix is found, the function should return an empty list.
    return submatrices
