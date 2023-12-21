
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices with sum 416
    submatrices = []
    
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary matrix to store the submatrix with sum 416
            temp_matrix = np.zeros((matrix.shape[0], matrix.shape[1]))
            
            # Calculate the sum of all integers in each submatrix
            sum_of_submatrix = np.sum(temp_matrix)
            
            # If the sum is 416, add the submatrix to the list of submatrices with sum 416
            if sum_of_submatrix == 416:
                submatrices.append(temp_matrix)
    
    return submatrices
