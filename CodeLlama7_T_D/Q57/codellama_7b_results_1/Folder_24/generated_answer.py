
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a variable to store the sum of the submatrix
            submatrix_sum = 0
            # Loop through each element of the submatrix
            for k in range(i, i + 3):
                for l in range(j, j + 3):
                    # Add the element to the sum of the submatrix
                    submatrix_sum += matrix[k][l]
            # If the sum of the submatrix equals -36, add it to the list of submatrices
            if submatrix_sum == -36:
                submatrices.append(submatrix_sum)
    return submatrices
