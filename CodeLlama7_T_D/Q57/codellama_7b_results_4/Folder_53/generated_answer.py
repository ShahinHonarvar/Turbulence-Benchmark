
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a variable to store the sum of the elements in the submatrix
            submatrix_sum = 0
            # Loop through each element in the submatrix
            for k in range(i, i + 2):
                for l in range(j, j + 2):
                    # Add the element to the sum
                    submatrix_sum += matrix[k][l]
            # If the sum of the elements in the submatrix equals -37, add the submatrix to the list of submatrices
            if submatrix_sum == -37:
                submatrices.append(matrix[i:i + 2, j:j + 2])
    # Return the list of submatrices
    return submatrices
