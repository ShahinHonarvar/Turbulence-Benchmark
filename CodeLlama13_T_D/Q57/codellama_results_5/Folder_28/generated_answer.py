
import numpy as np

def submatrix_with_particular_sum(mat):
    # Initialize an empty list to store the submatrices with sum 15
    submatrices = []
    
    # Loop through each row of the matrix
    for i in range(mat.shape[0]):
        # Loop through each column of the matrix
        for j in range(mat.shape[1]):
            # Initialize a temporary list to store the submatrix
            temp_list = []
            
            # Loop through each row and column of the submatrix
            for k in range(i, mat.shape[0]):
                for l in range(j, mat.shape[1]):
                    # Add the element to the temporary list
                    temp_list.append(mat[k, l])
            
            # Check if the sum of all elements in the temporary list is 15
            if np.sum(temp_list) == 15:
                # If it is, add the submatrix to the list of submatrices with sum 15
                submatrices.append(np.array(temp_list).reshape((k - i + 1, l - j + 1)))
    
    # Return the list of all submatrices with sum 15
    return submatrices
