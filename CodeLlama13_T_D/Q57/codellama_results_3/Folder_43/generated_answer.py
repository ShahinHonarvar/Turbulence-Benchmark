
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices with sum -81
    submatrices = []
    
    # Iterate over each submatrix of the given matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Initialize a temporary list to store the elements of the current submatrix
            temp_list = []
            
            # Iterate over each element of the current submatrix
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    # Add the current element to the temporary list
                    temp_list.append(matrix[k][l])
                    
                    # If the sum of all elements in the temporary list equals -81, add the submatrix to the list of submatrices with sum -81
                    if sum(temp_list) == -81:
                        submatrices.append(temp_list)
            
    return submatrices
