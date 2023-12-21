
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    
    # Get the shape of the input matrix
    rows, cols = matrix.shape
    
    # Loop through the matrix
    for i in range(rows):
        for j in range(cols):
            # Loop through all possible submatrix sizes
            for size in range(1, min(rows-i, cols-j)+1):
                # Get the submatrix
                submatrix = matrix[i:i+size, j:j+size]
                # Check if it contains 51 elements
                if np.size(submatrix) == 51:
                    count += 1
    return count
