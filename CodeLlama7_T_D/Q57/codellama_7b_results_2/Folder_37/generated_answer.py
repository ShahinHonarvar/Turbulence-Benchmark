
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
            for row in range(i, i + 2):
                for col in range(j, j + 2):
                    # Add the element to the sum of the elements in the submatrix
                    submatrix_sum += matrix[row][col]
            # Check if the sum of the elements in the submatrix equals -82
            if submatrix_sum == -82:
                # If the sum is equal to -82, add the submatrix to the list of submatrices
                submatrices.append(matrix[i:i + 2, j:j + 2])
    # Return the list of all submatrices that satisfy the condition
    return submatrices
