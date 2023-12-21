
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Convert the matrix to a list of lists for easier manipulation
    matrix = matrix.tolist()
    
    # Initialize an empty list to store the submatrices with the required sum
    submatrices = []
    
    # Iterate over each row in the matrix
    for i in range(len(matrix)):
        # Iterate over each column in the matrix
        for j in range(len(matrix[0])):
            # Initialize a temporary list to store the current submatrix
            temp_list = []
            
            # Iterate over each row and column of the submatrix, starting from (i, j)
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    # Add the current element to the temporary list
                    temp_list.append(matrix[k][l])
            
            # If the sum of all elements in the submatrix is -65, add it to the list of submatrices
            if sum(temp_list) == -65:
                submatrices.append(temp_list)
    
    return submatrices
