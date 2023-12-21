
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices with sum 126
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
                    # If the current element is within the bounds of the original matrix, add it to the temporary matrix
                    if i + k < matrix.shape[0] and j + l < matrix.shape[1]:
                        temp_matrix[k, l] = matrix[i + k, j + l]
                    
            # If the sum of all elements in the temporary matrix is 126, add it to the list of submatrices
            if np.sum(temp_matrix) == 126:
                submatrices.append(temp_matrix)
    
    return submatrices
