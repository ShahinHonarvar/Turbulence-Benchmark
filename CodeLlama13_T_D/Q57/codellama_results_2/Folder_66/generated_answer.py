
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the found submatrices
    submatrices = []
    
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary list to store the current submatrix
            temp_submatrix = []
            
            # Loop through each row and column of the current submatrix
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    # Add the current element to the temporary list
                    temp_submatrix.append(matrix[k, l])
            
            # Check if the sum of all elements in the temporary list is 99
            if np.sum(temp_submatrix) == 99:
                # If so, add the submatrix to the list of found submatrices
                submatrices.append(np.array(temp_submatrix).reshape((k-i+1, l-j+1)))
    
    # Return the list of found submatrices
    return submatrices
