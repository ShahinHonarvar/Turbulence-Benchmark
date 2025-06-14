
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

            # Calculate the sum of all elements in the submatrix
            for row in range(i, i + 3):
                for col in range(j, j + 3):
                    sum += matrix[row][col]

            # Check if the sum is equal to -261 and add the submatrix to the list if it is
            if sum == -261:
                submatrices.append((i, i + 3), (j, j + 3)))

    # Return the list of all submatrices that have a sum equal to -261, or an empty list if no such submatrix is found
    return submatrices
