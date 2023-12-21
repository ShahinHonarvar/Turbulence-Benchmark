
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices with the required sum
    submatrices = []
    
    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary list to store the current submatrix
            curr_submatrix = []
            
            # Iterate over each row and column of the submatrix
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    # Add the current element to the temporary list
                    curr_submatrix.append(matrix[k][l])
            
            # Check if the sum of all elements in the current submatrix is equal to -82
            if np.sum(curr_submatrix) == -82:
                # If so, add the current submatrix to the list of submatrices with the required sum
                submatrices.append(np.array(curr_submatrix))
    
    # Return the list of submatrices with the required sum
    return submatrices
