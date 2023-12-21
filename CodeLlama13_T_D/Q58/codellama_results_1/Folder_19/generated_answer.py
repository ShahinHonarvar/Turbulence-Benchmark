
import numpy as np

def submatrix_with_n_numbers(matrix, n):
    # Initialize a counter for the number of submatrices with n integers
    count = 0
    
    # Iterate over each row in the matrix
    for i in range(len(matrix)):
        # Iterate over each column in the current row
        for j in range(len(matrix[i])):
            # Check if the current element is equal to n
            if matrix[i][j] == n:
                # Increment the counter by 1
                count += 1
    
    return count
