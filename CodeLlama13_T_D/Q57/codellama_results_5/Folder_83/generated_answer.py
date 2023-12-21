
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices with a particular sum
    submatrices = []
    
    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary list to store the submatrix elements
            temp_list = []
            
            # Iterate over each row and column of the submatrix
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    # Add the element at the current row and column to the temporary list
                    temp_list.append(matrix[k][l])
            
            # Check if the sum of all elements in the submatrix is equal to -15
            if sum(temp_list) == -15:
                # If it is, add the submatrix to the list of submatrices with a particular sum
                submatrices.append(np.array(temp_list).reshape((k-i+1, l-j+1)))
    
    # Return the list of submatrices with a particular sum
    return submatrices
