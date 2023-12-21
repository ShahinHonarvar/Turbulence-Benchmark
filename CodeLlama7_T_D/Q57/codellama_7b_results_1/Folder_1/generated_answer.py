
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices with sum equal to -25
    submatrices = []
    # Iterate over each row in the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column in the matrix
        for j in range(matrix.shape[1]):
            # Find the sum of all integers in the submatrix with top-left corner at (i, j) and bottom-right corner at (m, n), where m and n are determined by the size of the submatrix
            sum = 0
            for row in range(i, i + 2):
                for col in range(j, j + 2):
                    if row < matrix.shape[0] and col < matrix.shape[1]:
                        sum += matrix[row][col]
            # If the sum is equal to -25, add the submatrix to the list of submatrices with sum equal to -25
            if sum == -25:
                submatrices.append(matrix[i: i + 2, j: j + 2])
    return submatrices
