
import numpy as np

def submatrix_with_n_numbers(matrix, n):
    # Initialize a counter for the number of submatrices with n integers
    count = 0
    
    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Check if the current element is equal to n
            if matrix[i, j] == n:
                # If it is, increment the counter and recursively call the function on the submatrix starting from this element
                count += 1
                count += submatrix_with_n_numbers(matrix[i+1:, j+1:], n)
    
    return count
