
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the output list
    submatrices = []

    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop over each column of the matrix
        for j in range(matrix.shape[1]):
            # Calculate the sum of all integers in the submatrix
            sum = 0
            for row in range(i, i + 3):
                for col in range(j, j + 3):
                    sum += matrix[row][col]

            # If the sum is equal to 394, add the submatrix to the output list
            if sum == 394:
                submatrices.append((i, i + 2), (j, j + 2)))

    return submatrices
