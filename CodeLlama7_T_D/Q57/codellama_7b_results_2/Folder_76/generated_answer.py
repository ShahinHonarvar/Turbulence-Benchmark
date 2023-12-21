
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []

    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a variable to store the sum of the elements in the submatrix
            sum = 0

            # Loop over each element in the submatrix
            for row in range(i, i + 3):
                for col in range(j, j + 3):
                    # Add the value of the current element to the sum
                    sum += matrix[row][col]

            # Check if the sum is equal to -255
            if sum == -255:
                # If it is, append the submatrix to the list of submatrices
                submatrices.append(matrix[i:i + 3, j:j + 3])

    # Return the list of submatrices
    return submatrices
