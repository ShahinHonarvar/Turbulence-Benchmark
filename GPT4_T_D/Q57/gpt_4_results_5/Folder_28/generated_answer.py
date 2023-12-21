
import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, columns = matrix.shape

    for submatrix_rows in range(1, rows+1):
        for submatrix_cols in range(1, columns+1):
            for i in range(rows - submatrix_rows + 1):
                for j in range(columns - submatrix_cols + 1):
                    submatrix = matrix[i:i+submatrix_rows, j:j+submatrix_cols]
                    if np.sum(submatrix) == 15:
                        result.append(submatrix.tolist())

    return result
