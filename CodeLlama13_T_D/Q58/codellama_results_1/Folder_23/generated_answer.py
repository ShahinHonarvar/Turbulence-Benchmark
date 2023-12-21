
import numpy as np

def submatrix_with_n_numbers(matrix, n):
    # Initialize an empty list to store the count of all submatrices with n numbers each
    submatrices = []
    
    # Iterate over all possible submatrices of the given matrix
    for i in range(matrix.shape[0] - n + 1):
        for j in range(matrix.shape[1] - n + 1):
            # Check if the current submatrix contains exactly n numbers
            if np.sum(matrix[i:i+n, j:j+n]) == n**2:
                # If so, add it to the list of submatrices with n numbers each
                submatrices.append((i, j))
    
    return len(submatrices)
