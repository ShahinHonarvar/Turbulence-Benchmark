
import numpy as np

def submatrix_with_n_numbers(matrix, n):
    # Initialize the count variable to zero
    count = 0
    
    # Loop over all rows and columns of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # If the current element is equal to n, increment the count
            if matrix[i][j] == n:
                count += 1
                
    # Return the count of submatrices containing n integers each
    return count
