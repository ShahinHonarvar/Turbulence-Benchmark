
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []
    
    # Iterate over each row in the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column in the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary list to store the current submatrix
            temp_submatrix = []
            
            # Iterate over each row and column of the submatrix starting from (i,j)
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    # Add the current element to the temporary list
                    temp_submatrix.append(matrix[k][l])
            
            # Check if the sum of all integers in the temporary submatrix is equal to 27
            if sum(temp_submatrix) == 27:
                # If it is, add the submatrix to the list of submatrices
                submatrices.append(temp_submatrix)
    
    # Return the list of submatrices
    return submatrices
