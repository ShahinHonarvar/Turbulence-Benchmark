
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the found submatrices
    found_submatrices = []
    
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary submatrix with size (i, j)
            temp_submatrix = np.zeros((i+1, j+1))
            
            # Fill the temporary submatrix with integers from the matrix
            for k in range(i+1):
                for l in range(j+1):
                    temp_submatrix[k, l] = matrix[k+i, l+j]
            
            # Check if the sum of all integers in the temporary submatrix is -936
            if np.sum(temp_submatrix) == -936:
                # If so, add the temporary submatrix to the found submatrices list
                found_submatrices.append(temp_submatrix)
    
    # Return the found submatrices list
    return found_submatrices
