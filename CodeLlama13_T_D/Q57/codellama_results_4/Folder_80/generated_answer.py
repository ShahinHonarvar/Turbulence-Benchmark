
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []
    
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary list to store the submatrix
            temp_submatrix = []
            
            # Add the current element to the temporary list
            temp_submatrix.append(matrix[i,j])
            
            # Loop through the remaining elements in the row and column
            for k in range(i+1, matrix.shape[0]):
                for l in range(j+1, matrix.shape[1]):
                    # Add the current element to the temporary list
                    temp_submatrix.append(matrix[k,l])
            
            # Check if the sum of all elements in the temporary list is equal to 245
            if sum(temp_submatrix) == 245:
                # Add the submatrix to the list of submatrices
                submatrices.append(np.array(temp_submatrix).reshape((k-i+1, l-j+1)))
    
    # Return the list of submatrices
    return submatrices
