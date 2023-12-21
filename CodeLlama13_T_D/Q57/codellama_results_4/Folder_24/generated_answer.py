
import numpy as np

def submatrix_with_particular_sum(mat):
    mat = np.array(mat)
    rows, cols = mat.shape
    
    for i in range(rows):
        for j in range(cols):
            if mat[i,j] == -36:
                return [mat[i:i+1, j:j+1]]
            
    return []
