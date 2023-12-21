
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the found submatrices
    submatrices = []
    
    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary list to store the current submatrix
            temp_submatrix = []
            
            # Add the current element to the temporary submatrix
            temp_submatrix.append(matrix[i,j])
            
            # Check if the sum of all elements in the temporary submatrix is equal to -4
            if np.sum(temp_submatrix) == -4:
                # If it is, add the current submatrix to the list of found submatrices
                submatrices.append(temp_submatrix)
                
    # Return the list of found submatrices
    return submatrices
