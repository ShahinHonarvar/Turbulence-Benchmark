
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []
    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a variable to store the sum of the submatrix
            sum = 0
            # Loop over each element of the submatrix
            for k in range(i, i + 3):
                for l in range(j, j + 3):
                    sum += matrix[k][l]
            # If the sum of the submatrix is equal to 21, add it to the list of submatrices
            if sum == 21:
                submatrices.append([matrix[i:i+3], matrix[j:j+3]])
    # Return the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals 21. If no such submatrix is found, the function should return an empty list.
    return submatrices
