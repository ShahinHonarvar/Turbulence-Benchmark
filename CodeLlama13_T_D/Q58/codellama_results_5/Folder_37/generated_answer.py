
import numpy as np

def submatrix_with_n_numbers(matrix, n):
    # Initialize a counter for the number of submatrices found
    count = 0
    
    # Loop over all possible starting positions in the matrix
    for i in range(matrix.shape[0] - n + 1):
        for j in range(matrix.shape[1] - n + 1):
            # Extract a submatrix of size n x n from the current position
            submatrix = matrix[i:i+n, j:j+n]
            
            # Check if the submatrix contains all integers between 0 and n-1
            if np.all(np.arange(n) == np.unique(submatrix)):
                count += 1
    
    return count
