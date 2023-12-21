
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []
    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a variable to store the sum of the elements in the submatrix
            submatrix_sum = 0
            # Iterate over each element in the submatrix
            for row in range(i, i + 3):
                for col in range(j, j + 3):
                    # Add the current element to the sum of the elements in the submatrix
                    submatrix_sum += matrix[row][col]
            # If the sum of the elements in the submatrix is -93, add it to the list of submatrices
            if submatrix_sum == -93:
                submatrices.append([matrix[i:i+3], matrix[j:j+3]]))
    # Return the list of submatrices that have a sum of -93
    return submatrices
