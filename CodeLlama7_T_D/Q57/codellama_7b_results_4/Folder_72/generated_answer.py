
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []
    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # Get the current row of the matrix
        row = matrix[i]
        # Loop over each column of the matrix
        for j in range(matrix.shape[1]):
            # Get the current column of the matrix
            col = matrix[:, j]
            # Check if the sum of all integers in the submatrix is equal to 41
            if np.sum(row) == 41 and np.sum(col) == 41:
                # If the sum is equal to 41, append the submatrix to the list of submatrices
                submatrices.append(matrix[i:i+1, j:j+1])
    # Return the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals 41. If no such submatrix is found, the function should return an empty list.
    return submatrices
