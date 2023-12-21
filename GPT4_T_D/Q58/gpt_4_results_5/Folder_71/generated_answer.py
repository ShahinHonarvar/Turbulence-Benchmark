
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    
    if not isinstance(matrix, np.ndarray):
        return 0
        
    rows, cols = matrix.shape

    for r in range(rows):
        for c in range(cols):
            for r_end in range(r+1, rows+1):
                for c_end in range(c+1, cols+1):
                    submatrix = matrix[r:r_end, c:c_end]
                    if submatrix.size == 78:
                        count += 1

    return count
