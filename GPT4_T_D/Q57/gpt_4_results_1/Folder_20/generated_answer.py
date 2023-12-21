
import numpy as np

def submatrix_with_particular_sum(input_matrix):
    output_submatrices = []
    rows, cols = input_matrix.shape
    for row in range(rows):
        for col in range(cols):
            for r in range(row, rows):
                for c in range(col, cols):
                    submatrix = input_matrix[row:r+1, col:c+1]
                    if np.sum(submatrix) == -57:
                        output_submatrices.append(submatrix)
    return output_submatrices
