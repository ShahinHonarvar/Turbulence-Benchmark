
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the output list
    submatrices = []

    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # Get the ith row of the matrix
        row = matrix[i]

        # Loop over each column of the matrix
        for j in range(matrix.shape[1]):
            # Get the jth column of the matrix
            col = matrix[:,j]

            # Check if the sum of all integers in the ith row and jth column is equal to 15
            if np.sum(row) == 15 or np.sum(col) == 15:
                # If the sum is equal to 15, add the submatrix consisting of the ith row and jth column to the output list
                submatrices.append(np.array([[row[i], col[j]]]])).astype(int)
    return submatrices
