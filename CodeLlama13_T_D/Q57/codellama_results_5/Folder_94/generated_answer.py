
import numpy as np

def submatrix_with_particular_sum(mat):
    # Initialize an empty list to store the submatrices with sum 92
    submatrices = []
    
    # Loop over each row of the matrix
    for i in range(mat.shape[0]):
        # Loop over each column of the matrix
        for j in range(mat.shape[1]):
            # Initialize a temporary list to store the current submatrix
            temp = []
            
            # Loop over each row of the submatrix starting from the current row
            for k in range(i, mat.shape[0]):
                # Loop over each column of the submatrix starting from the current column
                for l in range(j, mat.shape[1]):
                    # Add the current element to the temporary list
                    temp.append(mat[k][l])
                    
            # Check if the sum of all elements in the temporary list is equal to 92
            if np.sum(temp) == 92:
                # If it is, add the submatrix to the list of submatrices
                submatrices.append(temp)
                
    return submatrices
