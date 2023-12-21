
import numpy as np

def submatrix_with_particular_sum(matrix):
    nrows, ncols = matrix.shape
    result = []
    for width in range(ncols+1):
        for height in range(nrows+1):
            for i in range(ncols - width + 1):
                for j in range(nrows - height + 1):
                    submat = matrix[j:j+height, i:i+width]
                    if np.sum(submat) == 69:
                        result.append(submat)
    
    return result if len(result) > 0 else []
