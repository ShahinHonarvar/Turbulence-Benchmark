
import numpy as np

def submatrix_with_particular_sum(matrix):
    size = matrix.shape
    result = []
    for sub_size in range(1, min(size) + 1):
        for start_row in range(size[0] - sub_size + 1): 
            for start_col in range(size[1] - sub_size + 1): 
                submatrix = matrix[start_row:start_row + sub_size, start_col:start_col + sub_size]
                if np.sum(submatrix) == -936:
                    result.append(submatrix)

    return result
