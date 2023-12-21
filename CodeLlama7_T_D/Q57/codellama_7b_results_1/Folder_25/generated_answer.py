
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []

    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a variable to store the sum of the submatrix
            submatrix_sum = 0

            # Loop over each element of the submatrix
            for row in range(i, i + 3):
                for col in range(j, j + 3):
                    # Calculate the sum of the elements in the submatrix
                    submatrix_sum += matrix[row][col]

            # If the sum of the elements in the submatrix equals -20, add it to the list of submatrices
            if submatrix_sum == -20:
                submatrices.append(matrix[i:i + 3, j:j + 3])

    # Return the list of all submatrices that satisfy the condition
    return submatrices
