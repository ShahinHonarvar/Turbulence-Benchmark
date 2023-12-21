
import numpy as np
def submatrix_with_n_numbers(mat, n):
    """
    Returns the count of all submatrices of the given matrix that contain n integers each.
    If no such submatrix is found, 0 is returned.
    """
    # Get the dimensions of the input matrix
    rows = mat.shape[0]
    cols = mat.shape[1]
    
    # Initialize a counter for the number of submatrices with n integers
    count = 0
    
    # Iterate over each submatrix of size (n x n) in the input matrix
    for i in range(rows - n + 1):
        for j in range(cols - n + 1):
            # Extract the current submatrix and count its number of integers
            submat = mat[i:i+n, j:j+n]
            num_ints = np.count_nonzero(submat)
            
            # If the current submatrix contains n integers, increment the counter
            if num_ints == n:
                count += 1
    
    return count
