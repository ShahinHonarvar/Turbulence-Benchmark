
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Convert the matrix to a list of lists
    matrix = matrix.tolist()
    
    # Initialize an empty list to store the submatrices with the required sum
    submatrices = []
    
    # Loop through each row in the matrix
    for i in range(len(matrix)):
        # Loop through each column in the current row
        for j in range(len(matrix[i])):
            # Initialize a temporary list to store the current submatrix
            temp_submatrix = []
            
            # Add the current element to the temporary submatrix
            temp_submatrix.append(matrix[i][j])
            
            # Loop through each row below the current row in the matrix
            for k in range(i+1, len(matrix)):
                # Loop through each column in the current row
                for l in range(len(matrix[k])):
                    # Add the current element to the temporary submatrix
                    temp_submatrix.append(matrix[k][l])
            
            # Check if the sum of all integers in the temporary submatrix is -617
            if sum(temp_submatrix) == -617:
                # Add the temporary submatrix to the list of submatrices with the required sum
                submatrices.append(temp_submatrix)
    
    return submatrices
