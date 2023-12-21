
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the found submatrices
    submatrices = []
    
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a variable to store the current submatrix
            curr_submatrix = []
            
            # Add the current element to the submatrix
            curr_submatrix.append(matrix[i,j])
            
            # Loop through each row and column below the current one
            for k in range(i+1, matrix.shape[0]):
                for l in range(j+1, matrix.shape[1]):
                    # Add the current element to the submatrix
                    curr_submatrix.append(matrix[k,l])
            
            # Check if the sum of all elements in the current submatrix is equal to -811
            if np.sum(curr_submatrix) == -811:
                # If it is, add the submatrix to the list of found submatrices
                submatrices.append(curr_submatrix)
    
    # Return the list of found submatrices
    return submatrices
