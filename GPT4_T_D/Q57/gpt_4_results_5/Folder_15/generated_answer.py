
import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, columns = matrix.shape

    for row_start in range(rows):
        for column_start in range(columns):
            for row_end in range(row_start + 1, rows + 1):
                for column_end in range(column_start + 1, columns + 1):
                    sub_matrix = matrix[row_start:row_end, column_start:column_end]
                    if np.sum(sub_matrix) == -9:
                        result.append(sub_matrix.tolist())
                        
    return result
