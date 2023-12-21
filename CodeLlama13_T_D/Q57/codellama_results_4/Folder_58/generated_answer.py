
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the results
    result = []
    
    # Iterate over each row of the matrix
    for i in range(len(matrix)):
        # Iterate over each column of the current row
        for j in range(len(matrix[0])):
            # Calculate the sum of the submatrix starting from (i,j) and having size 3x3
            sum_submatrix = matrix[i][j] + matrix[i+1][j] + matrix[i+2][j] + \
                            matrix[i][j+1] + matrix[i+1][j+1] + matrix[i+2][j+1] + \
                            matrix[i][j+2] + matrix[i+1][j+2] + matrix[i+2][j+2]
            
            # If the sum of the submatrix is -137, add it to the result list
            if sum_submatrix == -137:
                result.append((i, j))
    
    return result
