
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the found submatrices
    found_submatrices = []
    
    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary submatrix with the current element as the top-left corner
            temp_submatrix = np.array([[matrix[i,j]]])
            
            # Check if the sum of all integers in the temporary submatrix equals -617
            if np.sum(temp_submatrix) == -617:
                # If so, add the temporary submatrix to the list of found submatrices
                found_submatrices.append(temp_submatrix)
            
            # Iterate over the remaining elements in the current row and column
            for k in range(i+1, matrix.shape[0]):
                for l in range(j+1, matrix.shape[1]):
                    # Extend the temporary submatrix by adding the current element as the bottom-right corner
                    temp_submatrix = np.append(temp_submatrix, [[matrix[k,l]]], axis=0)
                    
                    # Check if the sum of all integers in the temporary submatrix equals -617
                    if np.sum(temp_submatrix) == -617:
                        # If so, add the temporary submatrix to the list of found submatrices
                        found_submatrices.append(temp_submatrix)
    
    return found_submatrices
