
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize a list to store the submatrices with sum equal to 901
    submatrices = []
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a variable to store the sum of the submatrix
            sum = 0
            # Loop through each element of the submatrix
            for row in range(i, i + 3):
                for col in range(j, j + 3):
                    # Add the element to the sum
                    sum += matrix[row][col]
            # If the sum is equal to 901, add the submatrix to the list of submatrices with sum equal to 901
            if sum == 901:
                submatrices.append(matrix[i:i + 3, j:j + 3])
    # Return the list of submatrices with sum equal to 901
    return submatrices
