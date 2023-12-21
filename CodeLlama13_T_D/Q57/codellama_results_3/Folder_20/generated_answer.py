
import numpy as np

def submatrix_with_particular_sum(mat):
    # Initialize an empty list to store the submatrices with the required sum
    submatrices = []
    
    # Iterate over each row of the matrix
    for i in range(mat.shape[0]):
        # Iterate over each column of the matrix
        for j in range(mat.shape[1]):
            # Initialize a temporary list to store the current submatrix
            temp = []
            
            # Iterate over each row of the submatrix starting from the current row
            for k in range(i, mat.shape[0]):
                # Iterate over each column of the submatrix starting from the current column
                for l in range(j, mat.shape[1]):
                    # Add the current element to the temporary list
                    temp.append(mat[k][l])
            
            # Check if the sum of all elements in the temporary list is equal to -57
            if np.sum(temp) == -57:
                # If so, add the submatrix to the list of submatrices with the required sum
                submatrices.append(np.array(temp))
    
    # Return the list of submatrices with the required sum
    return submatrices
