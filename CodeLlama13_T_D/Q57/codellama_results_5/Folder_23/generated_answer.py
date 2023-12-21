
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the result
    submatrices = []
    
    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary list to store the current submatrix
            tmp = []
            
            # Add the current element to the temporary list
            tmp.append(matrix[i, j])
            
            # Iterate over the remaining elements of the row and column
            for k in range(i + 1, matrix.shape[0]):
                for l in range(j + 1, matrix.shape[1]):
                    # Add the current element to the temporary list
                    tmp.append(matrix[k, l])
            
            # Check if the sum of all integers in the temporary list is equal to 59
            if np.sum(tmp) == 59:
                # If so, add the temporary list to the submatrices list
                submatrices.append(tmp)
    
    # Return the submatrices list
    return submatrices
