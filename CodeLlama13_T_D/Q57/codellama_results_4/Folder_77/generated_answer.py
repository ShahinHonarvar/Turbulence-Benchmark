
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the found submatrices
    submatrices = []
    
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary submatrix with the current element as the first element
            tmp_submatrix = np.array([[matrix[i, j]]])
            
            # Loop through the remaining elements of the row and column
            for k in range(i+1, matrix.shape[0]):
                for l in range(j+1, matrix.shape[1]):
                    # Add the current element to the temporary submatrix
                    tmp_submatrix = np.append(tmp_submatrix, [[matrix[k, l]]], axis=0)
                    
                    # Check if the sum of all integers in the temporary submatrix equals -336
                    if np.sum(tmp_submatrix) == -336:
                        # If so, add the temporary submatrix to the list of found submatrices
                        submatrices.append(tmp_submatrix)
            
    return submatrices
