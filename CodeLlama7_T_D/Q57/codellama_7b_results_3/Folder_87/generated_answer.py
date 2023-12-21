
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []

    # Loop through each row of the matrix
    for i in range(len(matrix)):
        # Loop through each column of the matrix
        for j in range(len(matrix[i])):
            # Initialize a sum variable to store the sum of the integers in the submatrix
            sum = 0

            # Loop through each element of the submatrix
            for k in range(len(matrix)):
                # Add the integer at the current position to the sum variable
                sum += matrix[k][j]

            # If the sum of the integers in the submatrix equals 35, add the submatrix to the list of submatrices
            if sum == 35:
                submatrices.append(matrix[i][j]])

    # Return the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals 35. If no such submatrix is found, return an empty list.
    return submatrices
