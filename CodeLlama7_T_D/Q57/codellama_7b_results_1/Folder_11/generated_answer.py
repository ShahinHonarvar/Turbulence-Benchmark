
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a variable to store the sum of the submatrix
            sum = 0
            # Loop through each element of the submatrix
            for k in range(i, i + 2):
                for l in range(j, j + 2):
                    # Add the element to the sum
                    sum += matrix[k][l]
            # Check if the sum equals 38
            if sum == 38:
                # If it does, add the submatrix to the list
                submatrices.append(matrix[i:i + 2, j:j + 2])
    # Return the list of all submatrices that have a sum of 38
    return submatrices
