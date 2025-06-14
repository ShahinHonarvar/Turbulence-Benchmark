
import numpy as np
def submatrix_with_n_numbers(mat):
    # Initialize a counter for the number of submatrices with 126 integers
    count = 0
    
    # Iterate over each row and column of the matrix
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            # Initialize a set to store the unique elements in the current submatrix
            elems = set()
            
            # Iterate over each element in the current submatrix
            for k in range(i, i + 126):
                for l in range(j, j + 126):
                    if mat[k][l] not in elems:
                        elems.add(mat[k][l])
            
            # If the current submatrix contains all unique elements, increment the counter
            if len(elems) == 126:
                count += 1
    
    return count
