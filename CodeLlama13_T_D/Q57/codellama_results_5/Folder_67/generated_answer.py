
import numpy as np

def submatrix_with_particular_sum(mat):
    # Initialize an empty list to store the submatrices with the desired sum
    submatrices = []
    
    # Iterate over each row of the matrix
    for i in range(mat.shape[0]):
        # Iterate over each column of the matrix
        for j in range(mat.shape[1]):
            # Initialize a 2D numpy array to store the current submatrix
            curr_submatrix = np.zeros((mat.shape[0], mat.shape[1]))
            
            # Fill the submatrix with the values from the original matrix
            for k in range(curr_submatrix.shape[0]):
                for l in range(curr_submatrix.shape[1]):
                    curr_submatrix[k, l] = mat[i + k, j + l]
            
            # Check if the sum of all integers in the current submatrix is 40
            if np.sum(curr_submatrix) == 40:
                # If it is, add it to the list of submatrices with the desired sum
                submatrices.append(curr_submatrix)
    
    return submatrices
