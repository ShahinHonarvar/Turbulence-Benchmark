
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []
    
    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary list to store the submatrix
            temp_submatrix = []
            
            # Add the current element to the temporary list
            temp_submatrix.append(matrix[i, j])
            
            # Iterate over each element in the same row and column as the current element
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    # Add the current element to the temporary list
                    temp_submatrix.append(matrix[k, l])
            
            # Check if the sum of all integers in the temporary list is equal to 95
            if np.sum(temp_submatrix) == 95:
                # Add the temporary list to the submatrices list
                submatrices.append(temp_submatrix)
    
    # Return the submatrices list
    return submatrices
