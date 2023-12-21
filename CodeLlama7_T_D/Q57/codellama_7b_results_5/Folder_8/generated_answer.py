
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices
    submatrices = []

    # Loop through each row and column of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Initialize a submatrix with the current row and column
            submatrix = matrix[i:i+1, j:j+1]
            # Check if the sum of all integers in the submatrix equals -61
            if np.sum(submatrix) == -61:
                # Add the submatrix to the list of submatrices
                submatrices.append(submatrix)

    # Return the list of submatrices that satisfy the condition
    return submatrices
