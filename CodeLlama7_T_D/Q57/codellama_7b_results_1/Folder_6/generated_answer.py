
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
            for row in range(i, i + 2):
                for col in range(j, j + 2):
                    # Add the element to the sum if it is within the bounds of the matrix
                    if row < matrix.shape[0] and col < matrix.shape[1]:
                        sum += matrix[row][col]

            # If the sum equals the target value, add the submatrix to the list
            if sum == 126:
                submatrices.append(matrix[i:i + 2, j:j + 2])

    # Return the list of submatrices that satisfy the condition
    return submatrices
