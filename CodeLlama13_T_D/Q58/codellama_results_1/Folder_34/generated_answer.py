
import numpy as np

def submatrix_with_n_numbers(matrix, n):
    """
    Return the count of all submatrices of the given matrix that contain `n` integers each.
    If no such submatrix is found, return 0.
    """
    # Initialize a counter for the number of submatrices with `n` integers
    num_submatrices = 0
    
    # Iterate over the rows of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over the columns of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary matrix to store the submatrix
            temp_mat = np.zeros((n, n), dtype=np.int)
            
            # Fill the temporary matrix with the values from the original matrix
            for k in range(n):
                for l in range(n):
                    temp_mat[k][l] = matrix[i + k][j + l]
                    
            # Check if all elements of the submatrix are non-zero
            if np.all(temp_mat != 0):
                num_submatrices += 1
                
    return num_submatrices
