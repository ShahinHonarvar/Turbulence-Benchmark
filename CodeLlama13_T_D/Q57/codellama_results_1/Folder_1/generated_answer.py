
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the found submatrices
    found_submatrices = []
    
    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a submatrix with the current row and column indices
            submatrix = np.array([[matrix[i, j]]])
            
            # Check if the sum of all integers in the submatrix equals -25
            if np.sum(submatrix) == -25:
                # If so, add the submatrix to the list of found submatrices
                found_submatrices.append(submatrix)
            
            # Iterate over each subsequent row and column index
            for k in range(i+1, matrix.shape[0]):
                for l in range(j+1, matrix.shape[1]):
                    # Extend the current submatrix by adding the next row and column indices
                    submatrix = np.append(submatrix, [[matrix[k, l]]], axis=0)
                    
                    # Check if the sum of all integers in the extended submatrix equals -25
                    if np.sum(submatrix) == -25:
                        # If so, add the submatrix to the list of found submatrices
                        found_submatrices.append(submatrix)
    
    # Return the list of found submatrices
    return found_submatrices
