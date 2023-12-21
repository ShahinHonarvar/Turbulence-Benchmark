
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Convert the matrix to a list of lists for easier traversal
    mat = matrix.tolist()
    
    # Initialize an empty list to store the results
    result = []
    
    # Loop through each row and column of the matrix
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            # Calculate the sum of all integers in the submatrix starting from (i, j)
            curr_sum = 0
            for k in range(i, len(mat)):
                for l in range(j, len(mat[0])):
                    curr_sum += mat[k][l]
            
            # If the sum is -308, add the submatrix to the result list
            if curr_sum == -308:
                result.append(np.array(mat[i:k+1, j:l+1]))
    
    return result
