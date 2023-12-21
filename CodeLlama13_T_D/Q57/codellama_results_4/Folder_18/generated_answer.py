
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices with the particular sum
    submatrices = []
    
    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary list to store the submatrix
            temp_submatrix = []
            
            # Iterate over each row and column of the submatrix
            for k in range(i, matrix.shape[0]):
                temp_row = []
                for l in range(j, matrix.shape[1]):
                    # Add the element to the temporary list
                    temp_row.append(matrix[k][l])
                # Add the temporary row to the temporary submatrix
                temp_submatrix.append(temp_row)
            
            # Check if the sum of all integers in the submatrix is 616
            if np.sum(np.array(temp_submatrix)) == 616:
                # Add the submatrix to the list of submatrices with the particular sum
                submatrices.append(temp_submatrix)
    
    # Return the list of submatrices with the particular sum
    return submatrices
