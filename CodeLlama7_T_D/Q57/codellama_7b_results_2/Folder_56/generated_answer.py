
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []

    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a variable to store the sum of the submatrix
            submatrix_sum = 0

            # Iterate over each element of the submatrix
            for row in range(i, i + 2):
                for col in range(j, j + 2):
                    # Add the element to the submatrix sum
                    submatrix_sum += matrix[row][col]

            # If the submatrix sum equals -50, add the submatrix to the list of submatrices
            if submatrix_sum == -50:
                submatrices.append(matrix[i:i + 2, j:j + 2])

    # Return the list of submatrices that have a sum of all integers equal to -50
    return submatrices
