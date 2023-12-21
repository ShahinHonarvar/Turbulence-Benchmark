
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices with sum -6
    submatrices = []
    
    # Iterate over each row of the matrix
    for i in range(len(matrix)):
        # Iterate over each column of the matrix
        for j in range(len(matrix[0])):
            # Initialize a temporary submatrix with the current element as the first element
            temp_submatrix = [[matrix[i][j]]]
            
            # Check if the sum of all elements in the temporary submatrix is equal to -6
            if np.sum(temp_submatrix) == -6:
                # If so, add the submatrix to the list of submatrices
                submatrices.append(temp_submatrix)
            
            # Iterate over the remaining elements in the current row and column
            for k in range(i+1, len(matrix)):
                for l in range(j+1, len(matrix[0])):
                    # Add the element to the temporary submatrix
                    temp_submatrix.append([matrix[k][l]])
                    
                    # Check if the sum of all elements in the temporary submatrix is equal to -6
                    if np.sum(temp_submatrix) == -6:
                        # If so, add the submatrix to the list of submatrices
                        submatrices.append(temp_submatrix)
    
    return submatrices
