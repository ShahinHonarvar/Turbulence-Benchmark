
import numpy as np

def submatrix_with_particular_sum(matrix):
    if not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2:
        raise ValueError("The input should be a 2-d numpy array")
  
    result = []
    row, col = matrix.shape
    
    for row_size in range(1, row + 1):
        for col_size in range(1, col + 1):
            for i in range(row - row_size + 1):
                for j in range(col - col_size + 1):
                    submatrix = matrix[i:i + row_size, j:j + col_size]
                    if np.sum(submatrix) == -83:
                        result.append(submatrix)
                        
    return result
