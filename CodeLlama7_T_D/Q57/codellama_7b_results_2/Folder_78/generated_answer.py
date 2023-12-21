
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a variable to store the sum of the elements in the submatrix
            sum = 0
            # Loop through each element in the submatrix
            for k in range(i, i + 3):
                for l in range(j, j + 3):
                    # Add the element to the sum
                    sum += matrix[k][l]
            # If the sum of the elements in the submatrix equals 17, append the submatrix to the list of submatrices
            if sum == 17:
                submatrices.append(matrix[i:i + 3][j:j + 3]])
    # Return the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals 17. If no such submatrix is found, return an empty list.
    return submatrices
