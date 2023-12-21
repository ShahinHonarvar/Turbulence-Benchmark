
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape
    for sub_rows in range(rows):
        for sub_cols in range(cols):
            for size_cols in range(cols - sub_cols + 1):
                for size_rows in range(rows - sub_rows + 1):
                    if size_rows and size_cols:
                        submatrix = matrix[sub_rows:(sub_rows + size_rows),sub_cols:(sub_cols + size_cols)]
                        if np.sum(submatrix) == 17:
                            submatrices.append(submatrix.tolist())
    if not submatrices:
        return []
    
    return submatrices
