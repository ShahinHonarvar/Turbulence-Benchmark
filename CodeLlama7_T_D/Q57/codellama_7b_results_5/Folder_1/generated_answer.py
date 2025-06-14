
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices
    submatrices = []

    # Iterate over each row and column of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Get the submatrix with a size of 3x3 starting from the current position
            submatrix = matrix[i:i+3, j:j+3]
            # Check if the sum of all integers in the submatrix equals -25
            if np.sum(submatrix) == -25:
                # Add the submatrix to the list of submatrices
                submatrices.append(submatrix)

    return submatrices
