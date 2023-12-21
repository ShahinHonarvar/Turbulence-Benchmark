
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the found submatrices
    submatrices = []
    
    # Iterate over all rows of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over all columns of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary matrix to store the submatrix
            temp_matrix = np.zeros((matrix.shape[0] - i, matrix.shape[1] - j), dtype=np.int64)
            
            # Iterate over all rows of the temporary matrix
            for k in range(temp_matrix.shape[0]):
                # Iterate over all columns of the temporary matrix
                for l in range(temp_matrix.shape[1]):
                    # Add the value at position (i + k, j + l) to the temporary matrix
                    temp_matrix[k, l] = matrix[i + k, j + l]
            
            # Check if the sum of all integers in the temporary matrix equals -50
            if np.sum(temp_matrix) == -50:
                # If so, add the submatrix to the list of found submatrices
                submatrices.append(temp_matrix)
    
    return submatrices
