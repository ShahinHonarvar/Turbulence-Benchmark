
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices
    submatrices = []

    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a variable to store the sum of the submatrix
            submatrix_sum = 0

            # Loop through each element of the submatrix
            for k in range(i, i + 2):
                for l in range(j, j + 2):
                    # Add the element to the submatrix sum
                    submatrix_sum += matrix[k][l]

            # Check if the submatrix sum equals -10
            if submatrix_sum == -10:
                # Add the submatrix to the list of submatrices
                submatrices.append(submatrix)

    # Return the list of submatrices
    return submatrices
