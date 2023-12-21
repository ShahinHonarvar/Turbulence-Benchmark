
import numpy as np

def submatrix_with_particular_sum(matrix, sum):
    # Initialize an empty list to store the submatrices
    submatrices = []

    # Loop over the rows and columns of the matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # Extract a submatrix from the current row and column
            submatrix = matrix[i][j]

            # Check if the sum of the integers in the submatrix equals 382
            if np.sum(submatrix) == sum:
                # If it does, add the submatrix to the list of submatrices
                submatrices.append(submatrix)

    # Return the list of submatrices
    return submatrices
