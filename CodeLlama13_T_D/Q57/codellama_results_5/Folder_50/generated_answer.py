
import numpy as np

def submatrix_with_particular_sum(matrix):
    """
    Returns the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals 95. If no such submatrix is found, returns an empty list.
    """
    # Initialize an empty list to store the submatrices with a particular sum
    submatrices = []
    
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary list to store the current submatrix
            temp_submatrix = []
            
            # Add the current element to the temporary submatrix
            temp_submatrix.append([i, j])
            
            # Loop through each row and column of the matrix, starting from (i+1, j+1)
            for k in range(i+1, matrix.shape[0]):
                for l in range(j+1, matrix.shape[1]):
                    # Check if the sum of all integers in the current submatrix is equal to 95
                    if np.sum(matrix[temp_submatrix]) == 95:
                        # If so, add the current submatrix to the list of submatrices with a particular sum
                        submatrices.append(temp_submatrix)
                        
                    # Add the current element to the temporary submatrix
                    temp_submatrix.append([k, l])
    
    return submatrices
