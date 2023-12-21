
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the output list
    submatrices = []
    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a variable to store the sum of the submatrix
            submatrix_sum = 0
            # Loop over each row and column of the submatrix
            for k in range(i, i + 3):
                for l in range(j, j + 3):
                    # Add the current element to the sum of the submatrix
                    submatrix_sum += matrix[k][l]
            # If the sum of the submatrix is equal to 411, add it to the output list
            if submatrix_sum == 411:
                submatrices.append(matrix[i:i + 3][j:j + 3]])
    # Return the output list
    return submatrices
