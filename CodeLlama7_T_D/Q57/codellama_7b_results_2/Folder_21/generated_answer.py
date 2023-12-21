
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize a list to store the submatrices with sum -936
    submatrices = []
    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a variable to store the sum of the elements in the submatrix
            submatrix_sum = 0
            # Set the starting row and column indices for the submatrix
            start_row = i
            start_col = j
            # Iterate over each element in the submatrix
            for k in range(start_row, start_row + 3):
                for l in range(start_col, start_col + 3):
                    # Add the element to the sum of the elements in the submatrix
                    submatrix_sum += matrix[k][l]
            # Check if the sum of the elements in the submatrix is equal to -936
            if submatrix_sum == -936:
                # If it is, add the submatrix to the list of submatrices with sum -936
                submatrices.append(matrix[start_row:start_row + 3][start_col:start_col + 3]])
    # Return the list of submatrices with sum -936
    return submatrices
