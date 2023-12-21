
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count to 0
    count = 0
    # Loop over each row of the matrix
    for i in range(len(matrix)):
        # Loop over each column of the matrix
        for j in range(len(matrix[i])):
            # Check if the current element is equal to 193
            if matrix[i][j] == 193:
                # Increment the count by 1
                count += 1
    # Return the count of all submatrices with 193 elements each
    return count
