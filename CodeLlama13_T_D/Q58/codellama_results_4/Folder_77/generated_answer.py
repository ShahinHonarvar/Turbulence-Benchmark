
import numpy as np

def submatrix_with_n_numbers(matrix):
    # initialize a counter for the number of submatrices with 179 integers
    count = 0
    
    # loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # initialize a temporary matrix to store the submatrix
            temp_matrix = np.zeros((3, 3), dtype=int)
            
            # fill the temporary matrix with the values from the original matrix
            for k in range(3):
                for l in range(3):
                    temp_matrix[k, l] = matrix[i + k, j + l]
            
            # check if the temporary matrix contains 179 integers
            if np.sum(temp_matrix) == 179:
                count += 1
    
    return count
