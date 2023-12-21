
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices
    submatrices = []

    # Loop over each row and column of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Calculate the sum of all integers in the submatrix
            submatrix_sum = 0
            for k in range(i, i + 3):
                for l in range(j, j + 3):
                    submatrix_sum += matrix[k][l]

            # Check if the sum of all integers in the submatrix equals 752
            if submatrix_sum == 752:
                # If yes, add the submatrix to the list of submatrices
                submatrices.append(matrix[i:i + 3][j:j + 3]])

    # Return the list of all submatrices that satisfy the condition
    return submatrices
