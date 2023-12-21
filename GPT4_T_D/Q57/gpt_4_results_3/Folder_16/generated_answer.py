
import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, columns = matrix.shape
    for part_rows in range(1, rows + 1):
        for part_columns in range(1, columns + 1):
            for i in range(rows - part_rows + 1):
                for j in range(columns - part_columns + 1):
                    submatrix = matrix[i:i+part_rows, j:j+part_columns]
                    if np.sum(submatrix) == -157:
                        result.append(submatrix)
    return result
