
import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = np.shape(matrix)
    for sub_row in range(1, rows+1):
        for sub_col in range(1, cols+1):
            for i in range(rows+1-sub_row):
                for j in range(cols+1-sub_col):
                    submatrix = matrix[i:i+sub_row, j:j+sub_col]
                    if np.sum(submatrix) == -61:
                        result.append(submatrix)
    return result
