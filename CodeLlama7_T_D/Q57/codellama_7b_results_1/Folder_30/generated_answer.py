
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []

    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Extract the submatrix from the given matrix
            submatrix = matrix[i:, j:]

            # Calculate the sum of all integers in the submatrix
            submatrix_sum = np.sum(submatrix)

            # Check if the sum equals 21
            if submatrix_sum == 21:
                # Add the submatrix to the list of submatrices
                submatrices.append(submatrix)

    # Return the list of submatrices that have a sum of all integers equal to 21, or an empty list if no such submatrix is found
    return submatrices
