
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the output list
    submatrices = []

    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop over each column of the matrix
        for j in range(matrix.shape[1]):
            # Calculate the sum of all integers in the submatrix starting from (i, j)
            submatrix_sum = 0
            for k in range(i, i + 2):
                for l in range(j, j + 2):
                    submatrix_sum += matrix[k][l]

            # If the sum of all integers in the submatrix is equal to 64, add it to the output list
            if submatrix_sum == 64:
                submatrices.append(matrix[i:i + 2, j:j + 2])

    return submatrices
