
import numpy as np

def submatrix_with_n_numbers(matrix, n):
    # Initialize count to 0
    count = 0
    # Loop over all rows and columns of the matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # Check if the submatrix has the desired number of integers
            if len(set(matrix[i][j])) == n:
                count += 1
    
    return count
