
import numpy as np

def submatrix_with_particular_sum(matrix, sum_value):
    # Initialize an empty list to store the submatrices
    submatrices = []

    # Loop over all rows and columns of the matrix
    for row in range(matrix.shape[0]):
        for col in range(matrix.shape[1]):
            # Extract a submatrix from the current row and column
            submatrix = np.array([matrix[row, :], matrix[:, col]])

            # Check if the sum of all integers in the submatrix is equal to the specified value
            if np.sum(submatrix) == sum_value:
                # If so, add the submatrix to the list of submatrices
                submatrices.append(submatrix)

    # Return the list of all submatrices that have the specified sum
    return submatrices
