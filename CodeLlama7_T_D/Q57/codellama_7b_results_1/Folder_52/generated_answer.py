
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
                    # Add the element to the submatrix sum
                    submatrix_sum += matrix[k][l]
            # Check if the submatrix sum equals 100
            if submatrix_sum == 100:
                # If it does, add the submatrix to the list of submatrices
                submatrices.append(matrix[i:i + 3][j:j + 3]])
    # Return the list of all submatrices that have a sum of 100
    return submatrices
