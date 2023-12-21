
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices with sum 901
    submatrices = []
    
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary matrix to store the submatrix with sum 901
            temp_matrix = np.zeros((matrix.shape[0], matrix.shape[1]))
            
            # Loop through each row of the temporary matrix
            for k in range(temp_matrix.shape[0]):
                # Loop through each column of the temporary matrix
                for l in range(temp_matrix.shape[1]):
                    # If the current element is not zero, set it to the corresponding element of the original matrix
                    if temp_matrix[k, l] != 0:
                        temp_matrix[k, l] = matrix[i + k, j + l]
            
            # Check if the sum of all elements in the temporary matrix is equal to 901
            if np.sum(temp_matrix) == 901:
                # If it is, add the temporary matrix to the list of submatrices with sum 901
                submatrices.append(temp_matrix)
    
    # Return the list of submatrices with sum 901
    return submatrices
