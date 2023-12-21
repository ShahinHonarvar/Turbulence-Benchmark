
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices with the empty list
    submatrices = []

    # Iterate over each row in the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column in the matrix
        for j in range(matrix.shape[1]):
            # Initialize a new submatrix with the size of one cell
            submatrix = np.zeros((1, 1))

            # Add the current cell to the submatrix
            submatrix[0][0] = matrix[i][j]

            # Check if the sum of all integers in the submatrix equals -4
            if np.sum(submatrix) == -4:
                # If the condition is true, add the submatrix to the list of submatrices
                submatrices.append(submatrix)

    # Return the list of submatrices that satisfy the condition
    return submatrices
