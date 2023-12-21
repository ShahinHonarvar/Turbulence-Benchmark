
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize a counter for the number of submatrices with 107 integers
    count = 0
    
    # Loop through each row in the matrix
    for i in range(len(matrix)):
        # Loop through each column in the matrix
        for j in range(len(matrix[0])):
            # Check if the current element is 107
            if matrix[i][j] == 107:
                # If it is, increment the counter by 1
                count += 1
    
    return count
