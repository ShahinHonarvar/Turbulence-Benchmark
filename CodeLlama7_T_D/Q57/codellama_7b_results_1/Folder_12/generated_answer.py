
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize a list to store the submatrices with sum -83
    submatrices = []
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a variable to store the sum of all integers in the submatrix
            sum = 0
            # Loop through each element of the submatrix
            for row in range(i, i + 2):
                for col in range(j, j + 2):
                    # Add the value of the current element to the sum variable
                    sum += matrix[row][col]
            # If the sum is equal to -83, add the submatrix to the list of submatrices with that sum
            if sum == -83:
                submatrices.append(matrix[i:i + 2, j:j + 2])
    # Return the list of all submatrices with sum -83
    return submatrices
