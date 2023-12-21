
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
            for row in range(i, i + 2):
                for col in range(j, j + 2):
                    # Check if the current element is within the bounds of the matrix
                    if row < matrix.shape[0] and col < matrix.shape[1]:
                        # Add the current element to the submatrix sum
                        submatrix_sum += matrix[row, col]

            # Check if the submatrix sum is equal to 21
            if submatrix_sum == 21:
                # Add the submatrix to the list of submatrices
                submatrices.append(submatrix_sum)

    # Return the list of submatrices that have a sum of 21
    return submatrices
