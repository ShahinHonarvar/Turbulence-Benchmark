
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []

    for submatrix_row in range(1, rows+1):
        for submatrix_col in range(1, cols+1):
            for row in range(rows - submatrix_row + 1):
                for col in range(cols - submatrix_col + 1):
                    submatrix = matrix[row:(row+submatrix_row), 
                                       col:(col+submatrix_col)]
                    if np.sum(submatrix) == 77:
                        result.append(submatrix)
    return result
