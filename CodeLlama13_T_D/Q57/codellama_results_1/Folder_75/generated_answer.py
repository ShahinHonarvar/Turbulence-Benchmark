
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices with sum 16
    submatrices = []
    
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary matrix to store the submatrix
            temp_matrix = np.zeros((matrix.shape[0], matrix.shape[1]), dtype=int)
            
            # Loop through each row of the temporary matrix
            for k in range(temp_matrix.shape[0]):
                # Loop through each column of the temporary matrix
                for l in range(temp_matrix.shape[1]):
                    # If the current element is not the first element of the submatrix, set it to 0
                    if k != i or l != j:
                        temp_matrix[k, l] = 0
                    
                    # Otherwise, set it to the corresponding element of the matrix
                    else:
                        temp_matrix[k, l] = matrix[k, l]
            
            # If the sum of all elements in the temporary matrix is 16, add it to the list of submatrices
            if np.sum(temp_matrix) == 16:
                submatrices.append(temp_matrix)
    
    # Return the list of submatrices with sum 16
    return submatrices
