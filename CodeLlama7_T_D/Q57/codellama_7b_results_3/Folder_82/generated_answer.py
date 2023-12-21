
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a variable to store the sum of the submatrix
            submatrix_sum = 0
            # Define the bounds of the submatrix
            start_row = i
            end_row = i + 2
            start_col = j
            end_col = j + 2
            # Check if the submatrix is valid (i.e., it does not extend beyond the boundaries of the matrix)
            if start_row >= 0 and end_row <= matrix.shape[0] and start_col >= 0 and end_col <= matrix.shape[1]:
                # Loop through each element of the submatrix
                for k in range(start_row, end_row):
                    for l in range(start_col, end_col):
                        # Add the element to the sum of the submatrix
                        submatrix_sum += matrix[k][l]
            # If the submatrix has the required sum (-27), add it to the list of submatrices
            if submatrix_sum == -27:
                submatrices.append(matrix[start_row:end_row, start_col:end_col])
    # Return the list of all submatrices with the required sum (-27)
    return submatrices
