
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []
    
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a variable to store the current submatrix
            curr_submatrix = []
            
            # Loop through each row of the submatrix
            for k in range(i, matrix.shape[0]):
                # Loop through each column of the submatrix
                for l in range(j, matrix.shape[1]):
                    # Add the current element to the submatrix
                    curr_submatrix.append(matrix[k][l])
            
            # Check if the sum of all integers in the current submatrix is equal to 69
            if np.sum(curr_submatrix) == 69:
                # If it is, add the submatrix to the list of submatrices
                submatrices.append(curr_submatrix)
    
    # Return the list of all submatrices with a particular sum
    return submatrices
