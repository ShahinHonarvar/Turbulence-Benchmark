
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices with zeros
    submatrices = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    # Loop through each row and column of the matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # Initialize a variable to store the sum of the submatrix
            submatrix_sum = 0
            # Loop through each element of the submatrix
            for row in range(i, i + 3):
                for col in range(j, j + 3):
                    # Add the current element to the submatrix sum
                    submatrix_sum += matrix[row][col]
            # Check if the submatrix sum equals 93
            if submatrix_sum == 93:
                # Append the submatrix to the list of submatrices
                submatrices.append(matrix[i:i + 3, j:j + 3])
    # Return the list of submatrices with a sum equal to 93
    return submatrices
