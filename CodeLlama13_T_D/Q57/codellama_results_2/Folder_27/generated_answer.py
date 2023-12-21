
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Create a list of all possible submatrices with given size
    submatrices = []
    for i in range(matrix.shape[0] - 1):
        for j in range(matrix.shape[1] - 1):
            submatrices.append(np.array([matrix[i:i+2,j:j+2]]))
    
    # Iterate over all submatrices and check if their sum is equal to 77
    for sub in submatrices:
        if np.sum(sub) == 77:
            return sub
    return []
