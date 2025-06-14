
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices with a particular sum
    submatrices = []
    
    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary matrix to store the current submatrix
            temp_mat = np.zeros((matrix.shape[0], matrix.shape[1]))
            
            # Set the elements of the temporary matrix to the corresponding elements of the original matrix
            for k in range(temp_mat.shape[0]):
                for l in range(temp_mat.shape[1]):
                    temp_mat[k, l] = matrix[i + k, j + l]
            
            # Check if the sum of all elements in the temporary matrix is 997
            if np.sum(temp_mat) == 997:
                # If it is, add the submatrix to the list of submatrices
                submatrices.append(temp_mat)
    
    # Return the list of submatrices with a particular sum
    return submatrices
