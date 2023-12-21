
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices with sum 8
    submatrices = []
    
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary matrix to store the submatrix with sum 8
            temp_matrix = np.zeros((matrix.shape[0], matrix.shape[1]))
            
            # Loop through each row of the temporary matrix
            for k in range(temp_matrix.shape[0]):
                # Loop through each column of the temporary matrix
                for l in range(temp_matrix.shape[1]):
                    # Calculate the sum of all integers in the submatrix
                    temp_sum = np.sum(temp_matrix[k:k+i, l:l+j])
                    
                    # If the sum is 8, add the submatrix to the list of submatrices
                    if temp_sum == 8:
                        submatrices.append(temp_matrix[k:k+i, l:l+j].tolist())
    
    return submatrices
