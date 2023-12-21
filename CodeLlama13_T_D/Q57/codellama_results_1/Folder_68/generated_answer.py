
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices with sum 3
    submatrices = []
    
    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary list to store the submatrix elements
            temp = []
            
            # Iterate over each row and column of the submatrix
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    # Add the element at (k, l) to the temporary list
                    temp.append(matrix[k][l])
            
            # Check if the sum of all elements in the submatrix is 3
            if np.sum(temp) == 3:
                # If so, add the submatrix to the list of submatrices with sum 3
                submatrices.append((i, j, k, l))
    
    return submatrices
