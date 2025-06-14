
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize a count variable to keep track of the number of submatrices found
    count = 0
    
    # Loop through each row and column of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Check if the current element is equal to 66
            if matrix[i, j] == 66:
                # If it is, then check if there are exactly 66 elements in a submatrix starting from this element
                if np.sum(np.diagonal(matrix[i:i+6, j:j+6])) == 66:
                    count += 1
    
    # Return the number of submatrices found
    return count
