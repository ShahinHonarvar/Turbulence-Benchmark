
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a counter to keep track of the sum
            sum = 0
            # Loop through each element of the submatrix
            for k in range(i, i + 3):
                for l in range(j, j + 3):
                    # Add the element to the sum
                    sum += matrix[k][l]
            # If the sum is equal to the target sum, add the submatrix to the list
            if sum == 94:
                submatrices.append(matrix[i:i + 3, j:j + 3])
    # Return the list of submatrices
    return submatrices
