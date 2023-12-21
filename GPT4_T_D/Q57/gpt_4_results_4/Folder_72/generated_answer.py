
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices_with_sum_41 = []
    
    for sub_rows in range(1, rows+1):
        for sub_cols in range(1, cols+1):
            for r in range(rows - sub_rows + 1):
                for c in range(cols - sub_cols + 1):
                    submatrix = matrix[r:r+sub_rows, c:c+sub_cols]
                    if np.sum(submatrix) == 41:
                        submatrices_with_sum_41.append(submatrix)
                        
    return submatrices_with_sum_41
