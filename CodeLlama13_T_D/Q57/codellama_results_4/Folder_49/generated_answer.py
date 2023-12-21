
import numpy as np

def submatrix_with_particular_sum(mat):
    # Initialize an empty list to store the submatrices with the desired sum
    submatrices = []
    
    # Iterate over each submatrix of the given matrix
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            # Initialize a temporary matrix to store the current submatrix
            temp_mat = np.zeros((i+1, j+1), dtype=int)
            
            # Copy the elements of the original matrix to the temporary matrix
            for k in range(temp_mat.shape[0]):
                for l in range(temp_mat.shape[1]):
                    temp_mat[k, l] = mat[i-k, j-l]
            
            # Check if the sum of all integers in the current submatrix is equal to -42
            if np.sum(temp_mat) == -42:
                # If yes, add the submatrix to the list of submatrices with the desired sum
                submatrices.append(temp_mat)
    
    # Return the list of all submatrices with the desired sum
    return submatrices
