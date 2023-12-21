
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a variable to store the sum of the elements in the submatrix
            submatrix_sum = 0
            # Loop through each element in the submatrix
            for row in range(i, i + 3):
                for col in range(j, j + 3):
                    # Check if the element is within the boundaries of the matrix
                    if row < matrix.shape[0] and col < matrix.shape[1]:
                        # Add the element to the sum of the submatrix
                        submatrix_sum += matrix[row][col]
            # Check if the sum of the elements in the submatrix equals -20
            if submatrix_sum == -20:
                # Append the submatrix to the list of submatrices
                submatrices.append(matrix[i:i + 3, j:j + 3])
    # Return the list of submatrices that satisfy the condition
    return submatrices
