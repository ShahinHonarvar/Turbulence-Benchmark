
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices
    submatrices = []

    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Get the submatrix starting from (i, j)
            submatrix = matrix[i:, j:]

            if np.sum(submatrix) == 2:
                # Add the submatrix to the list of submatrices
                submatrices.append(submatrix)

    return submatrices
