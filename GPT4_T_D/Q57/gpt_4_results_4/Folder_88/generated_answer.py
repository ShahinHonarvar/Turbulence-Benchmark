
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    
    for size_row in range(1, rows + 1):
        for size_col in range(1, cols + 1):
            for start_row in range(rows - size_row + 1):
                for start_col in range(cols - size_col + 1):
                    submatrix = matrix[start_row:(start_row + size_row), start_col:(start_col + size_col)]
                    
                    if np.sum(submatrix) == -64:
                        result.append(submatrix.tolist())
                        
    return result
