
import numpy as np

def submatrix_with_n_numbers(matrix, n):
    # Initialize the count to 0
    count = 0
    # Iterate over all rows and columns of the matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # Check if the current submatrix contains n integers
            if len(set(matrix[i][j])) == n:
                # Increment the count by 1
                count += 1
    # Return the final count
    return count
