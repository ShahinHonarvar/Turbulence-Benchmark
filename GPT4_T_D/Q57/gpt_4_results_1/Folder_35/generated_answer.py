
import numpy as np

def submatrix_with_particular_sum(matrix):
    results = []
    rows,cols = matrix.shape
    for dim_row in range(1,rows+1):
        for dim_col in range(1,cols+1):
            for i in range(rows-dim_row+1):
                for j in range(cols-dim_col+1):
                    submatrix = matrix[i:i+dim_row,j:j+dim_col]
                    if np.sum(submatrix) == 432:
                        results.append(submatrix)
    return results
