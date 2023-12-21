
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the found submatrices
    found_submatrices = []
    
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary list to store the current submatrix
            temp_submatrix = []
            
            # Add the current element to the temporary submatrix
            temp_submatrix.append(matrix[i,j])
            
            # Loop through the remaining elements in the row and column
            for k in range(i+1, matrix.shape[0]):
                for l in range(j+1, matrix.shape[1]):
                    # If the sum of the current submatrix is equal to 66, add it to the found submatrices list
                    if np.sum(temp_submatrix) == 66:
                        found_submatrices.append(np.array(temp_submatrix))
                        
                    # Add the current element to the temporary submatrix and continue looping
                    temp_submatrix.append(matrix[k,l])
    
    # Return the list of found submatrices
    return found_submatrices
