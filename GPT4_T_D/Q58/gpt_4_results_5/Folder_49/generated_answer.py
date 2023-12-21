
import numpy as np 

def submatrix_with_n_numbers(matrix):
    if type(matrix) is not np.ndarray:
        return 0
      
    rows,cols = matrix.shape
    count = 0
    for r in range(1,rows+1):
        for c in range(1,cols+1):
            if r*c == 72:
                count += (rows - r + 1) * (cols - c + 1)
    
    return count
