
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices
    submatrices = []

    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a variable to store the sum of the submatrix
            submatrix_sum = 0

            # Calculate the starting and ending indices of the submatrix
            start_row = i - 2 if i >= 3 else 0
            end_row = i + 3 if i + 3 < matrix.shape[0] else matrix.shape[0]
            start_col = j - 2 if j >= 3 else 0
            end_col = j + 3 if j + 3 < matrix.shape[1] else matrix.shape[1]

            # Iterate over each element of the submatrix
            for row in range(start_row, end_row):
                for col in range(start_col, end_col):
                    # Add the element to the sum of the submatrix
                    submatrix_sum += matrix[row][col]

            # If the sum of the submatrix is equal to 830, add it to the list of submatrices
            if submatrix_sum == 830:
                submatrices.append([row for row in range(start_row, end_row)])

    # Return the list of submatrices
    return submatrices
