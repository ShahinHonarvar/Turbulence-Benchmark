
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []
    # Loop through each row of the matrix
    for i in range(len(matrix)):
        # Loop through each column of the matrix
        for j in range(len(matrix[i])):
            # Initialize a variable to store the sum of the current submatrix
            submatrix_sum = 0
            # Loop through each element of the current submatrix
            for row in range(i, i + 3):
                for col in range(j, j + 3):
                    # Add the element to the sum of the current submatrix
                    submatrix_sum += matrix[row][col]
            # If the sum of the current submatrix equals -38, add it to the list of submatrices
            if submatrix_sum == -38:
                submatrices.append(matrix[i:i + 3][j:j + 3])
    # Return the list of all submatrices with a sum equal to -38, or an empty list if no such submatrix is found
    return submatrices
