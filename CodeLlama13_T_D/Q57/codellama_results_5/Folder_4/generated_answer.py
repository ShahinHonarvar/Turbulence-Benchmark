
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices with the particular sum
    submatrices = []
    
    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary list to store the submatrix
            temp_submatrix = []
            
            # Add the current element to the temporary list
            temp_submatrix.append(matrix[i,j])
            
            # Iterate over the remaining elements in the row and column
            for k in range(i+1, matrix.shape[0]):
                for l in range(j+1, matrix.shape[1]):
                    # Add the current element to the temporary list
                    temp_submatrix.append(matrix[k,l])
            
            # Check if the sum of all elements in the temporary list is equal to 87
            if np.sum(temp_submatrix) == 87:
                # Add the submatrix to the list of submatrices
                submatrices.append(temp_submatrix)
    
    # Return the list of submatrices with the particular sum
    return submatrices
