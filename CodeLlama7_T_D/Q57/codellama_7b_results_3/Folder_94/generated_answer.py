
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []

    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Extract the submatrix of size 2x2 starting at position (i, j)
            submatrix = matrix[i:i+2, j:j+2]

            # Check if the sum of all integers in the submatrix is equal to 92
            if np.sum(submatrix) == 92:
                # If the condition is true, append the submatrix to the list of submatrices
                submatrices.append(submatrix)

    return submatrices
