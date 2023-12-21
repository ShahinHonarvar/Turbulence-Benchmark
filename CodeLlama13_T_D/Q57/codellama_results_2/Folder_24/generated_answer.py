
import numpy as np

def submatrix_with_particular_sum(mat):
    # Initialize an empty list to store the results
    result = []
    
    # Loop through each row of the matrix
    for i in range(mat.shape[0]):
        # Loop through each column of the matrix
        for j in range(mat.shape[1]):
            # Initialize a temporary matrix to store the current submatrix
            temp_mat = np.zeros((mat.shape[0], mat.shape[1]))
            
            # Calculate the sum of all integers in each submatrix
            submatrix_sum = np.sum(temp_mat[i:, j:])
            
            # If the sum is equal to -36, add the current submatrix to the results list
            if submatrix_sum == -36:
                result.append((i, j))
    
    # Return the results list
    return result
