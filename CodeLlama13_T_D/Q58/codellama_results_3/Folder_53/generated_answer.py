
import numpy as np
def submatrix_with_n_numbers(matrix):
    # Initialize a counter for the number of submatrices with 24 integers
    count = 0
    
    # Loop through each row and column of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Check if the current element is equal to 1
            if matrix[i, j] == 1:
                # Get the submatrix with a size of 24 elements by slicing the matrix
                submatrix = matrix[i:i+24, j:j+24]
                
                # Check if all elements in the submatrix are equal to 1
                if np.all(submatrix == 1):
                    count += 1
    
    return count
