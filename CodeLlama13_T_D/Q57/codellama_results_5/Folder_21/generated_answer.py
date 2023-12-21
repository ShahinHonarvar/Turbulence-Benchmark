
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices with the required sum
    submatrices = []
    
    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary list to store the current submatrix
            temp_submatrix = []
            
            # Add the current element to the temporary submatrix
            temp_submatrix.append(matrix[i, j])
            
            # Iterate over the remaining elements in the row and column
            for k in range(i+1, matrix.shape[0]):
                for l in range(j+1, matrix.shape[1]):
                    # Add the current element to the temporary submatrix
                    temp_submatrix.append(matrix[k, l])
            
            # Check if the sum of all elements in the temporary submatrix is equal to -936
            if sum(temp_submatrix) == -936:
                # If it is, add the temporary submatrix to the list of submatrices
                submatrices.append(temp_submatrix)
    
    # Return the list of submatrices with the required sum
    return submatrices
