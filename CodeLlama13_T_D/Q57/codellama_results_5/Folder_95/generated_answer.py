
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []
    
    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a variable to store the current submatrix
            current_submatrix = np.array([])
            
            # Iterate over each row of the submatrix
            for k in range(i, matrix.shape[0]):
                # Iterate over each column of the submatrix
                for l in range(j, matrix.shape[1]):
                    # Add the current element to the submatrix
                    current_submatrix = np.append(current_submatrix, matrix[k,l])
            
            # Check if the sum of all integers in the current submatrix is 19
            if np.sum(current_submatrix) == 19:
                # If it is, add the submatrix to the list of submatrices
                submatrices.append(current_submatrix)
    
    # Return the list of submatrices
    return submatrices
